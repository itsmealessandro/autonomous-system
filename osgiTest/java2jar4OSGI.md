# From a .java to a bundle for osgi

## Requirements
Osgi libs:
```
org.apache.felix.gogo.command_1.1.2.jar
org.apache.felix.gogo.runtime_1.1.6.jar
org.apache.felix.gogo.shell_1.1.4.jar
org.eclipse.equinox.console_1.4.800.v20240513-1104.jar
org.eclipse.osgi_3.21.0.v20240717-2103.jar
```
with its config.ini file:
```
osgi.bundles=org.eclipse.osgi_3.21.0.v20240717-2103.jar@start, org.eclipse.equinox.console_1.4.800.v20240513-1104.jar@start, org.apache.felix.gogo.command_1.1.2.jar@start, org.apache.felix.gogo.shell_1.1.4.jar@start, org.apache.felix.gogo.runtime_1.1.6.jar@start
osgi.noShutdown=true
eclipse.ignoreApp=true
```

We use testOsgi.java for the example.
```
import org.osgi.framework.BundleActivator;
import org.osgi.framework.BundleContext;

public class testOsgi implements BundleActivator {

  @Override
  public void start(BundleContext bc) {
    System.out.println("Bundle has started, I'm alive");
  }

  @Override
  public void stop(BundleContext context) {
    System.out.println("Bundle is stopping.");
  }
}
```


## 1: compile .java
```
javac -cp org.eclipse.osgi_3.21.0.v20240717-2103.jar -d . testOsgi.java
```

## 2: create a MANIFEST.MF
the content of the MANIFEST.MF file should contain at least:
```
Bundle-ManifestVersion: 2
Bundle-Name: Test OSGi Bundle
Bundle-SymbolicName: test.bundle
Bundle-Version: 1.0.0
Bundle-Activator: testOsgi
Import-Package: org.osgi.framework
```

## 3: generate the jar
```
jar cfm testOsgi.jar MANIFEST.MF testOsgi.class     
```

## 4: open the osgi console
```
java -jar org.eclipse.osgi_3.21.0.v20240717-2103.jar -console          
```

## 5: install the jar
```
install file:testOsgi.jar
```

## 5: start the bundle
```
start <ID_BUNDLE>
```
