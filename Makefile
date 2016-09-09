PKG_NAME := jdk-parboiled
URL := https://github.com/sirthias/parboiled/archive/1.1.6.tar.gz
ARCHIVES := http://repo1.maven.org/maven2/org/parboiled/parboiled-core/1.1.6/parboiled-core-1.1.6.pom %{buildroot} \
	http://repo1.maven.org/maven2/org/parboiled/parboiled-java/1.1.6/parboiled-java-1.1.6.pom %{buildroot} \
	http://repo1.maven.org/maven2/org/parboiled/parboiled-scala_2.10/1.1.6/parboiled-scala_2.10-1.1.6.pom %{buildroot}

include ../common/Makefile.common
