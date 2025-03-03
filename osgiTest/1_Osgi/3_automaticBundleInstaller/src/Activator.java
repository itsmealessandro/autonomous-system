import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import org.osgi.framework.Bundle;
import org.osgi.framework.BundleActivator;
import org.osgi.framework.BundleContext;
import org.osgi.framework.BundleException;

/*
 * This class has the goal of installing in osgi the Bundle "testOsgi.jar" if is in the directory defined by the PATH*/
public class Activator implements BundleActivator {

  private static final long INTERVAL = 5000;
  private static final String BUNDLE = "testOsgi.jar";
  private static final String PATH = "/home/alessandro/Desktop/Università/magistrale/1_anno/as/autonomous-system/osgiTest/1_Osgi/3_automaticBundleInstaller/";

  private Thread thread;
  private static BundleContext context;
  private long lastModifiedTime = 0; // Per tenere traccia dell'ultima modifica

  static BundleContext getContext() {
    return context;
  }

  @Override
  public void start(BundleContext bundleContext) throws Exception {
    Activator.context = bundleContext;
    System.out.println("Bundle started!");

    // Avvia il thread per monitorare il file
    startBundleUpdater();

    // Scrive nel file di log quando il bundle parte
    FileWriter hello_file = new FileWriter("BundleFileLog.txt");
    hello_file.write("I just started");
    hello_file.close();
  }

  @Override
  public void stop(BundleContext bundleContext) throws Exception {
    Activator.context = null;
    if (thread != null) {
      thread.interrupt();
    }
    System.out.println("Bundle stopping...");

    // Scrive nel file di log quando il bundle si ferma
    FileWriter hello_file = new FileWriter("BundleStop.txt");
    hello_file.write("I just stopped");
    hello_file.close();
  }

  private void startBundleUpdater() {
    thread = new Thread(() -> {
      try {
        System.out.println("[DEBUG] Runnable started");
        String location = PATH + BUNDLE;

        File file = new File(location);

        while (!Thread.currentThread().isInterrupted()) {
          Thread.sleep(INTERVAL); // Dorme per 5 secondi

          System.out.println("Checking for file...");
          if (file.exists()) {
            // Verifica se il file è stato modificato
            long fileModified = file.lastModified();
            if (fileModified > lastModifiedTime) {
              // Se il file è stato modificato, installa il nuovo bundle
              System.out.println("File is newer, installing the bundle...");
              installNewBundle(location);
              lastModifiedTime = fileModified; // Aggiorna il timestamp dell'ultima modifica
            } else {
              System.out.println("No change in the file, skipping installation.");
            }
          } else {
            System.out.println("Bundle file not found.");
          }
        }
      } catch (InterruptedException e) {
        System.out.println("[DEBUG] Thread interrupted.");
      }
    });
    thread.start();
  }

  private void installNewBundle(String location) {
    try {
      System.out.println("Installing bundle from location: " + location);
      // Installa il nuovo bundle
      Bundle bundle = context.installBundle("file:///" + location); // Aggiungi 'file:///' per il percorso locale
      System.out.println("Bundle installed: " + bundle.getSymbolicName());
      bundle.start(); // Puoi avviare il bundle subito dopo l'installazione
    } catch (BundleException e) {
      System.out.println("Error installing bundle from " + location);
      e.printStackTrace();
    }
  }
}
