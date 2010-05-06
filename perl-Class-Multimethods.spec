%define upstream_name    Class-Multimethods
%define upstream_version 1.70

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A multiple dispatch mechanism for Perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The Class:Multimethod module exports a subroutine (&multimethod) that can
be used to declare other subroutines that are dispatched using a algorithm
different from the normal Perl subroutine or method dispatch mechanism.

Normal Perl subroutines are dispatched by finding the appropriately-named
subroutine in the current (or specified) package and calling that. Normal
Perl methods are dispatched by attempting to find the appropriately-named
subroutine in the package into which the invoking object is blessed or,
failing that, recursively searching for it in the packages listed in the
appropriate '@ISA' arrays.

Class::Multimethods multimethods are dispatched quite differently. The
dispatch mechanism looks at the classes or types of each argument to the
multimethod (by calling 'ref' on each) and determines the "closest"
matching _variant_ of the multimethod, according to the argument types
specified in the variants' definitions (see the Finding the "nearest"
multimethod manpage for a definition of "closest").

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


