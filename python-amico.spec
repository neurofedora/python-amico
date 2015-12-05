%global modname amico

Name:           python-%{modname}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Relationships (e.g. friendships) backed by Redis

License:        MIT
URL:            https://pypi.python.org/pypi/amico
Source0:        https://pypi.python.org/packages/source/a/amico/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python2-setuptools
BuildRequires:  python-redis
Requires:       python-redis

%description -n python2-%{modname}
%{summary}.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-redis
Requires:       python3-redis

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -c
mv %{modname}-%{version} python2

rm -rf python2/*.egg-info

cp -a python2 python3
2to3 --write --nobackups python3

%build
pushd python2
  %py2_build
popd

pushd python3
  %py3_build
popd

%install
pushd python2
  %py2_install
popd

pushd python3
  %py3_install
popd

%files -n python2-%{modname}
%license python2/LICENSE.txt
%doc python2/README.md
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license python3/LICENSE.txt
%doc python3/README.md
%{python3_sitelib}/%{modname}*

%changelog
* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.1-1
- Initial package
