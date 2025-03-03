# OSGi Manifest (`MANIFEST.MF`) - Explanation of Fields

The `MANIFEST.MF` file of an OSGi bundle contains essential information for the OSGi framework. Below, each field is explained with its function and whether it is mandatory or optional.

## 📌 **Mandatory Fields**

### `Bundle-ManifestVersion`
```properties
Bundle-ManifestVersion: 2
```
- **Description:** Specifies the version of the OSGi standard for the manifest. The value "2" is the latest.
- **Mandatory:** ✅ Yes

### `Bundle-SymbolicName`
```properties
Bundle-SymbolicName: it.univaq.disim.se4as.bundleupdater-extended
```
- **Description:** Unique name of the bundle in the OSGi system. It follows Java package naming conventions.
- **Mandatory:** ✅ Yes

### `Bundle-Version`
```properties
Bundle-Version: 1.0.0.qualifier
```
- **Description:** Version of the bundle. The "qualifier" can be replaced with a build identifier.
- **Mandatory:** ✅ Yes

## ⚠️ **Highly Recommended Fields**

### `Bundle-Activator`
```properties
Bundle-Activator: it.univaq.disim.se4as.bundleupdater_extended.Activator
```
- **Description:** Class that runs at the start and stop of the bundle.
- **Mandatory:** ❌ No (but necessary if you want to execute code on activation)

### `Import-Package`
```properties
Import-Package: org.osgi.framework;version="1.3.0"
```
- **Description:** Lists external packages required by the bundle. Here, `org.osgi.framework` is requested.
- **Mandatory:** ❌ No (but necessary if the bundle depends on external packages)

## 🛠 **Optional Fields**

### `Bundle-Name`
```properties
Bundle-Name: Bundleupdater-extended
```
- **Description:** Human-readable name of the bundle. Descriptive only.
- **Mandatory:** ❌ No

### `Bundle-RequiredExecutionEnvironment`
```properties
Bundle-RequiredExecutionEnvironment: JavaSE-1.8
```
- **Description:** Specifies the required Java runtime environment (e.g., Java 8).
- **Mandatory:** ❌ No

### `Bundle-ActivationPolicy`
```properties
Bundle-ActivationPolicy: lazy
```
- **Description:** If set to `lazy`, the bundle is activated only when needed.
- **Mandatory:** ❌ No (if not specified, the bundle activates immediately)

## 📝 **Important Notes**
- **Comments are not supported** directly in `MANIFEST.MF`. You can document in separate files or in the code.
- If the bundle **does not have a `Bundle-Activator`**, it can still function if it only provides services or resources.
- If the bundle uses external classes, **`Import-Package` is mandatory** to avoid runtime errors.

🚀 **With this information, you can properly configure an OSGi bundle!**
