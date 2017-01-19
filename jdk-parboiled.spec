Name     : jdk-parboiled
Version  : 1.1.6
Release  : 2
URL      : https://github.com/sirthias/parboiled/archive/1.1.6.tar.gz
Source0  : https://github.com/sirthias/parboiled/archive/1.1.6.tar.gz
Source1  : http://repo1.maven.org/maven2/org/parboiled/parboiled-core/1.1.6/parboiled-core-1.1.6.pom
Source2  : http://repo1.maven.org/maven2/org/parboiled/parboiled-java/1.1.6/parboiled-java-1.1.6.pom
Source3  : parboiled-pom.xml
Source4  : http://repo1.maven.org/maven2/org/parboiled/parboiled-scala_2.10/1.1.6/parboiled-scala_2.10-1.1.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Patch0   : parboiled-1.1.6-scala-use-antrun-plugin.patch
Patch1   : parboiled-port-to-objectweb-asm-5.0.1.patch
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-aqute-bndlib
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-eclipse-eclipse
BuildRequires : jdk-eclipse-osgi
BuildRequires : jdk-eclipse-osgi-services
BuildRequires : jdk-felix
BuildRequires : jdk-felix-bundlerepository
BuildRequires : jdk-felix-framework
BuildRequires : jdk-felix-osgi-core
BuildRequires : jdk-felix-osgi-foundation
BuildRequires : jdk-felix-utils
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-kxml
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-antrun-plugin
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-bundle-plugin
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-osgi-compendium
BuildRequires : jdk-osgi-core
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-scala-compiler
BuildRequires : jdk-scala-library
BuildRequires : jdk-scala-parser-combinators_2.11
BuildRequires : jdk-scala-reflect
BuildRequires : jdk-scala-xml_2.11
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy
BuildRequires : jdk-snappy-java
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : jdk-xz
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
# Please see
* <http://repo1.maven.org/maven2/org/parboiled/> for download access to the artifacts
* <http://wiki.github.com/sirthias/parboiled> for all documentation
* <http://users.parboiled.org> for the user mailing list / forum
* <http://sirthias.github.com/parboiled/api/core> for the parboiled-core API javadoc
* <http://sirthias.github.com/parboiled/api/java> for the parboiled-java API javadoc
* <http://sirthias.github.com/parboiled/api/scala> for the parboiled-scala API scaladoc
* <http://github.com/sirthias/parboiled/wiki/Patch-Policy> for the Patch Policy

%prep
%setup -q -n parboiled-1.1.6

find . -name "*.class" -delete
find . -name "*.jar" -delete

cp -p  %{SOURCE1} parboiled-core/pom.xml
cp -p  %{SOURCE2} parboiled-java/pom.xml
cp -p  %{SOURCE4} parboiled-scala/pom.xml

for m in core java; do
python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   "pom:project" "

<build>
  <plugins>

  </plugins>
</build>" parboiled-${m}

python3 /usr/share/java-utils/pom_editor.py pom_add_plugin     org.apache.maven.plugins:maven-jar-plugin parboiled-${m} "

<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"
done

python3 /usr/share/java-utils/pom_editor.py pom_add_plugin     org.apache.felix:maven-bundle-plugin parboiled-core "

<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.parboiled.core</Bundle-SymbolicName>
    <Bundle-Name>org.parboiled.core</Bundle-Name>
    <Bundle-Version>\${project.version}</Bundle-Version>
    <Private-Package>org.parboiled.core.*</Private-Package>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

python3 /usr/share/java-utils/pom_editor.py pom_add_plugin     org.apache.felix:maven-bundle-plugin parboiled-java "

<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.parboiled.java</Bundle-SymbolicName>
    <Bundle-Name>org.parboiled.java</Bundle-Name>
    <Bundle-Version>\${project.version}</Bundle-Version>
    <Fragment-Host>org.parboiled.core</Fragment-Host>
    <Private-Package>org.parboiled.java.*</Private-Package>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

%patch0 -p0
%patch1 -p1

cp -p %{SOURCE3} pom.xml
sed -i "s|@VERSION@|1.1.6|" pom.xml

python3 /usr/share/java-utils/mvn_file.py :parboiled-core parboiled/core
python3 /usr/share/java-utils/mvn_file.py :parboiled-java parboiled/java
python3 /usr/share/java-utils/mvn_package.py :parboiled-project __noinstall
python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   "pom:modules" "<module>parboiled-scala</module>"
python3 /usr/share/java-utils/mvn_file.py :parboiled-scala_2.10 parboiled/scala
python3 /usr/share/java-utils/mvn_package.py :parboiled-scala_2.10 scala

%build
python3 /usr/share/java-utils/mvn_build.py   -f -- -Dproject.build.sourceEncoding=UTF-8

%install
xmvn-install  -R .xmvn-reactor -n parboiled -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/parboiled/core.jar
/usr/share/java/parboiled/java.jar
/usr/share/java/parboiled/scala.jar
/usr/share/maven-metadata/parboiled-scala.xml
/usr/share/maven-metadata/parboiled.xml
/usr/share/maven-poms/parboiled/core.pom
/usr/share/maven-poms/parboiled/java.pom
/usr/share/maven-poms/parboiled/scala.pom
