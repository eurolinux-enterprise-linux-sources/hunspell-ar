%global upstreamid 20080110

Summary: Arabic hunspell dictionaries
Name: hunspell-ar
Version: 0.%{upstreamid}
Release: 10%{?dist}
License: GPLv2 or LGPLv2 or MPLv1.1
Group: Applications/Text
URL: http://ayaspell.sourceforge.net/
Source: http://downloads.sourceforge.net/ayaspell/hunspell-ar_%{upstreamid}.tar.gz

BuildArch: noarch
Requires: hunspell

%description
Arabic (Egypt, Algeria, etc.) hunspell dictionaries.

%prep
%setup -q -n %{name}_%{upstreamid}

%build
# nothing to build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ar.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ar_TN.dic
cp -p ar.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ar_TN.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ar_TN_aliases="ar_AE ar_BH ar_DJ ar_DZ ar_EG ar_ER ar_IL ar_IN ar_IQ ar_JO ar_KM ar_KW ar_LB ar_LY ar_MA ar_MR ar_OM ar_PS ar_QA ar_SA ar_SD ar_SO ar_SY ar_TD ar_YE"
for lang in $ar_TN_aliases; do
    ln -s ar_TN.aff $lang.aff
    ln -s ar_TN.dic $lang.dic
done
popd

%files
%doc AUTHORS ChangeLog-ar COPYING README-ar THANKS
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20080110-10
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080110-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Peter Schiffer <pschiffe@redhat.com> - 0.20080110-8
- .spec file cleanup

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080110-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080110-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080110-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080110-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 06 2009 Caolan McNamara <caolanm@redhat.com> - 0.20080110-3
- extend aliases

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080110-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr 28 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080110-1
- use the much lighter ayaspell data instead of Buckwalter

* Wed Jun 06 2007 Caolan McNamara <caolanm@redhat.com> - 0.20060208-1
- initial version
