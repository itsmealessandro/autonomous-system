# From a .java to a .jar
We use test.java for the example.

## 1: compile .java
```
javac test.java
```

## 2: create a MANIFEST.MF
the content of the MANIFEST.MF file should contain at least:
```
Manifest-Version: 1.0
Main-Class: test
```

## 3: generate the jar
```
jar cvfm test1.jar MANIFEST.MF test.class
```
```
