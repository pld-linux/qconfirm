Summary:	qconfirm - request delivery confirmation for mail
Summary(pl.UTF-8):   qconfirm - żądanie potwierdzenia dostarczenia poczty
Name:		qconfirm
Version:	0.14.3
Release:	0.1
License:	BSD
Group:		Applications/File
Source0:	http://smarden.org/qconfirm/%{name}-%{version}.tar.gz
# Source0-md5:	e41edae19b2b9244b5d0ae62cf41f947
URL:		http://smarden.org/qconfirm/
Requires:	qmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/qmail

%description
qconfirm is an implementation of a delivery confirmation process for a
mailing list or mail address. It is invoked by qmail-local through a
dot-qmail file, and can reduce the amount of junk mail hitting a
mailbox or the mailboxes of mailing list subscribers. qconfirm
performs this delivery confirmation process either sender based or
message based.

%description -l pl.UTF-8
qconfirm to implementacja procesu potwierdzenia dostarczenia dla list
lub adresów pocztowych. Jest wywoływany przez qmail-local poprzez plik
dot-qmail i może zmniejszyć ilość niechcianej poczty trafiającej do
skrzynek użytkowników bądź subskrybentów list pocztowych. qconfirm
przeprowadza proces potwierdzenia dostarczenia w oparciu o nadawcę lub
wiadomość.

%prep
%setup -q -n mail

%build
cd %{name}-%{version}
echo '%{__cc} %{rpmcflags}' > src/conf-cc
echo '%{__cc}' > src/conf-ld
./package/compile

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
install -d $RPM_BUILD_ROOT{%{_libexecdir},%{_mandir}/man1}

cp -a man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install command/* $RPM_BUILD_ROOT%{_libexecdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libexecdir}/qconfirm
%{_libexecdir}/qconfirm-accept
%{_libexecdir}/qconfirm-cdb-check
%{_libexecdir}/qconfirm-cdb-update
%{_libexecdir}/qconfirm-check
%{_libexecdir}/qconfirm-check-mid
%{_libexecdir}/qconfirm-conf
%{_libexecdir}/qconfirm-control
%{_libexecdir}/qconfirm-inject
%{_libexecdir}/qconfirm-notice
%{_libexecdir}/qconfirm-return
%{_mandir}/man1/qconfirm-accept.1*
%{_mandir}/man1/qconfirm-cdb-check.1*
%{_mandir}/man1/qconfirm-cdb-update.1*
%{_mandir}/man1/qconfirm-check-mid.1*
%{_mandir}/man1/qconfirm-check.1*
%{_mandir}/man1/qconfirm-conf.1*
%{_mandir}/man1/qconfirm-control.1*
%{_mandir}/man1/qconfirm-inject.1*
%{_mandir}/man1/qconfirm-notice.1*
%{_mandir}/man1/qconfirm-return.1*
%{_mandir}/man1/qconfirm.1*
