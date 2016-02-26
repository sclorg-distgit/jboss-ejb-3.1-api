%global pkg_name jboss-ejb-3.1-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.0.2
Release:          10.12%{?dist}
Summary:          EJB 3.1 API
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-ejb-api_spec.git jboss-ejb-3.1-api
# cd jboss-ejb-3.1-api/ && git archive --format=tar --prefix=jboss-ejb-3.1-api/ jboss-ejb-api_3.1_spec-1.0.2.Final | xz > jboss-ejb-3.1-api-1.0.2.Final.tar.xz
Source0:          jboss-ejb-3.1-api-%{namedversion}.tar.xz

BuildRequires:    %{?scl_prefix}jboss-transaction-1.1-api
BuildRequires:    %{?scl_prefix}jboss-jaxrpc-1.1-api
BuildRequires:    %{?scl_prefix}jboss-specs-parent
BuildRequires:    %{?scl_prefix_java_common}javapackages-tools
BuildRequires:    %{?scl_prefix}maven-local
BuildRequires:    %{?scl_prefix}maven-compiler-plugin
BuildRequires:    %{?scl_prefix}maven-install-plugin
BuildRequires:    %{?scl_prefix}maven-jar-plugin
BuildRequires:    %{?scl_prefix}maven-javadoc-plugin
BuildRequires:    %{?scl_prefix}maven-enforcer-plugin
BuildRequires:    %{?scl_prefix}maven-dependency-plugin

BuildArch:        noarch

%description
The Java EJB 3.1 API classes.

%package javadoc
Summary:          Javadocs for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n jboss-ejb-3.1-api
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 1.0.2-10.12
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.0.2-10.11
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.0.2-10.10
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0.2-10.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0.2-10.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-10.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-10.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-10.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-10.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-10.3
- SCL-ize build-requires
- Migrate from mvn-rpmbuild to %%mvn_build

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-10.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-10.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.2-10
- Mass rebuild 2013-12-27

* Fri Dec 13 2013 Ade Lee <alee@redhat.com> 1.0.2-9
- Fix spec file dist tag for rpmlint

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-8
- Remove unneeded BR: maven-plugin-cobertura

* Thu May 9 2013 Ade Lee <alee@redhat.com> 1.0.2-7
- Resolves #961454 - Remove unneeded maven-checkstyle-plugin BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.2-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Nov 29 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-4
- Remove unneeded BR: maven-eclipse-plugin

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.3-1
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.2-1
- Upstream release 1.0.2.Final

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.2-0.1.20120309git53fbe3
- Packaging after license cleanup upstream

* Fri Aug 12 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-2
- Using geronimo-jta instead of jboss-transactions

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Initial packaging

