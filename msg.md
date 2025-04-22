BUILD SUCCESSFUL in 19s
1 actionable task: 1 executed
Subproject Path: CordovaLib
Subproject Path: app
Downloading https://services.gradle.org/distributions/gradle-7.1.1-all.zip
..............10%...............20%...............30%...............40%..............50%...............60%...............70%...............80%..............90%...............100%

Welcome to Gradle 7.1.1!

Here are the highlights of this release:
 - Faster incremental Java compilation
 - Easier source set configuration in the Kotlin DSL

For more details see https://docs.gradle.org/7.1.1/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)

FAILURE: Build failed with an exception.

* Where:
Settings file '/home/runner/work/Ace-Code/Ace-Code/platforms/android/settings.gradle'

* What went wrong:
Could not compile settings file '/home/runner/work/Ace-Code/Ace-Code/platforms/android/settings.gradle'.
> startup failed:
  General error during conversion: Unsupported class file major version 61
  
  java.lang.IllegalArgumentException: Unsupported class file major version 61
  	at groovyjarjarasm.asm.ClassReader.<init>(ClassReader.java:189)
  	at groovyjarjarasm.asm.ClassReader.<init>(ClassReader.java:170)
  	at groovyjarjarasm.asm.ClassReader.<init>(ClassReader.java:156)
  	at groovyjarjarasm.asm.ClassReader.<init>(ClassReader.java:277)
  	at org.codehaus.groovy.ast.decompiled.AsmDecompiler.parseClass(AsmDecompiler.java:81)
  	at org.codehaus.groovy.control.ClassNodeResolver.findDecompiled(ClassNodeResolver.java:251)
  	at org.codehaus.groovy.control.ClassNodeResolver.tryAsLoaderClassOrScript(ClassNodeResolver.java:189)
  	at