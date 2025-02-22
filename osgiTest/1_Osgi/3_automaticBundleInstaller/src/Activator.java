import java.io.File;

import org.osgi.framework.Bundle;
import org.osgi.framework.BundleActivator;
import org.osgi.framework.BundleContext;
import org.osgi.framework.BundleException;

public class Activator implements BundleActivator {

  private static final long INTERVAL = 5000;
  private static final String BUNDLE = ".";

  private final Thread thread = new Thread(new BundleUpdater());
  private static BundleContext context;

  static BundleContext getContext() {
    return context;
  }

  /*
   * (non-Javadoc)
   * 
   * @see
   * org.osgi.framework.BundleActivator#start(org.osgi.framework.BundleContext)
   */
  public void start(BundleContext bundleContext) throws Exception {
    Activator.context = bundleContext;
    thread.start();
  }

  /*
   * (non-Javadoc)
   * 
   * @see
   * org.osgi.framework.BundleActivator#stop(org.osgi.framework.BundleContext)
   */
  public void stop(BundleContext bundleContext) throws Exception {
    Activator.context = null;
    thread.interrupt();
  }

  protected Bundle findBundleByLocation(String location) {
    Bundle[] bundles = context.getBundles();
    for (int i = 0; i < bundles.length; i++) {
      if (bundles[i].getLocation().equals(location)) {
        return bundles[i];
      }
    }
    return null;
  }

  private class BundleUpdater implements Runnable {
    public void run() {
      try {
        File file = new File(BUNDLE);
        String location = "file:///" + BUNDLE;
        while (!Thread.currentThread().isInterrupted()) {
          Thread.sleep(INTERVAL);
          Bundle bundle = findBundleByLocation(location);
          if (bundle != null && file.exists()) {
            long bundleModified = bundle.getLastModified();
            long fileModified = file.lastModified();
            if (fileModified > bundleModified) {
              System.out.println("File is newer, updating.");
              bundle.update();
            }
          }
        }
      } catch (InterruptedException e) {
        System.out.println("I'm going now.");
      } catch (BundleException e) {
        System.out.println("Error updating bundle.");
        e.printStackTrace();
      }
*/
    }
  }
}
