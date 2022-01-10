#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Industrial strength alternative to OCaml's standard library
Summary(pl.UTF-8):	Przemysłowy zamiennik biblioteki standardowej OCamla
Name:		ocaml-core_kernel
Version:	0.14.2
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/core_kernel/tags
Source0:	https://github.com/janestreet/core_kernel/archive/v%{version}/core_kernel-%{version}.tar.gz
# Source0-md5:	ede2f6d22eaa8320f88bac67d41b5cff
URL:		https://github.com/janestreet/core_kernel
BuildRequires:	ocaml >= 1:4.08.0
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-base_bigstring-devel >= 0.14
BuildRequires:	ocaml-base_bigstring-devel < 0.15
BuildRequires:	ocaml-base_quickcheck-devel >= 0.14
BuildRequires:	ocaml-base_quickcheck-devel < 0.15
BuildRequires:	ocaml-bin_prot-devel >= 0.14
BuildRequires:	ocaml-bin_prot-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-fieldslib-devel >= 0.14
BuildRequires:	ocaml-fieldslib-devel < 0.15
BuildRequires:	ocaml-jane-street-headers-devel >= 0.14
BuildRequires:	ocaml-jane-street-headers-devel < 0.15
BuildRequires:	ocaml-jst-config-devel >= 0.14
BuildRequires:	ocaml-jst-config-devel < 0.15
BuildRequires:	ocaml-ppx_assert-devel >= 0.14
BuildRequires:	ocaml-ppx_assert-devel < 0.15
BuildRequires:	ocaml-ppx_base-devel >= 0.14
BuildRequires:	ocaml-ppx_base-devel < 0.15
BuildRequires:	ocaml-ppx_hash-devel >= 0.14
BuildRequires:	ocaml-ppx_hash-devel < 0.15
BuildRequires:	ocaml-ppx_inline_test-devel >= 0.14
BuildRequires:	ocaml-ppx_inline_test-devel < 0.15
BuildRequires:	ocaml-ppx_jane-devel >= 0.14
BuildRequires:	ocaml-ppx_jane-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_conv-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_message-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_message-devel < 0.15
BuildRequires:	ocaml-sexplib-devel >= 0.14
BuildRequires:	ocaml-sexplib-devel < 0.15
BuildRequires:	ocaml-splittable_random-devel >= 0.14
BuildRequires:	ocaml-splittable_random-devel < 0.15
BuildRequires:	ocaml-stdio-devel >= 0.14
BuildRequires:	ocaml-stdio-devel < 0.15
BuildRequires:	ocaml-time_now-devel >= 0.14
BuildRequires:	ocaml-time_now-devel < 0.15
BuildRequires:	ocaml-typerep-devel >= 0.14
BuildRequires:	ocaml-typerep-devel < 0.15
BuildRequires:	ocaml-variantslib-devel >= 0.14
BuildRequires:	ocaml-variantslib-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Core suite of libraries is an industrial strength alternative to
OCaml's standard library that was developed by Jane Street, the
largest industrial user of OCaml.

Core_kernel is the system-independent part of Core.

This package contains files needed to run bytecode executables using
core_kernel library.

%description -l pl.UTF-8
Zbiór bibliotek Core to przemysłowy zamiennik biblioteki standardowej
OCamla, tworzony przez Jane Street, największego przemysłowego
użytkownika OCamla.

Core_kernel to niezależna od systemu część Core.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki core_kernel.

%package devel
Summary:	Industrial strength alternative to OCaml's standard library - development part
Summary(pl.UTF-8):	Przemysłowy zamiennik biblioteki standardowej OCamla - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-base_bigstring-devel >= 0.14
Requires:	ocaml-base_quickcheck-devel >= 0.14
Requires:	ocaml-bin_prot-devel >= 0.14
Requires:	ocaml-fieldslib-devel >= 0.14
Requires:	ocaml-jane-street-headers-devel >= 0.14
Requires:	ocaml-jst-config-devel >= 0.14
Requires:	ocaml-ppx_assert-devel >= 0.14
Requires:	ocaml-ppx_base-devel >= 0.14
Requires:	ocaml-ppx_hash-devel >= 0.14
Requires:	ocaml-ppx_inline_test-devel >= 0.14
Requires:	ocaml-ppx_jane-devel >= 0.14
Requires:	ocaml-ppx_sexp_conv-devel >= 0.14
Requires:	ocaml-ppx_sexp_message-devel >= 0.14
Requires:	ocaml-sexplib-devel >= 0.14
Requires:	ocaml-splittable_random-devel >= 0.14
Requires:	ocaml-stdio-devel >= 0.14
Requires:	ocaml-time_now-devel >= 0.14
Requires:	ocaml-typerep-devel >= 0.14
Requires:	ocaml-variantslib-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
core_kernel library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki core_kernel.

%prep
%setup -q -n core_kernel-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/core_kernel/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/core_kernel/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/core_kernel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md INRIA-DISCLAIMER.txt LICENSE.md MLton-license.txt README.md THIRD-PARTY.txt strftime.js-licence.txt
%dir %{_libdir}/ocaml/core_kernel
%{_libdir}/ocaml/core_kernel/META
%{_libdir}/ocaml/core_kernel/runtime.js
%{_libdir}/ocaml/core_kernel/strftime.js
%{_libdir}/ocaml/core_kernel/*.cma
%dir %{_libdir}/ocaml/core_kernel/ansi_kernel
%{_libdir}/ocaml/core_kernel/ansi_kernel/*.cma
%dir %{_libdir}/ocaml/core_kernel/balanced_reducer
%{_libdir}/ocaml/core_kernel/balanced_reducer/*.cma
%dir %{_libdir}/ocaml/core_kernel/base_for_tests
%{_libdir}/ocaml/core_kernel/base_for_tests/*.cma
%dir %{_libdir}/ocaml/core_kernel/binary_packing
%{_libdir}/ocaml/core_kernel/binary_packing/*.cma
%dir %{_libdir}/ocaml/core_kernel/bounded_int_table
%{_libdir}/ocaml/core_kernel/bounded_int_table/*.cma
%dir %{_libdir}/ocaml/core_kernel/bus
%{_libdir}/ocaml/core_kernel/bus/*.cma
%dir %{_libdir}/ocaml/core_kernel/caml_unix
%{_libdir}/ocaml/core_kernel/caml_unix/*.cma
%dir %{_libdir}/ocaml/core_kernel/composition_infix
%{_libdir}/ocaml/core_kernel/composition_infix/*.cma
%dir %{_libdir}/ocaml/core_kernel/enum
%{_libdir}/ocaml/core_kernel/enum/*.cma
%dir %{_libdir}/ocaml/core_kernel/fheap
%{_libdir}/ocaml/core_kernel/fheap/*.cma
%dir %{_libdir}/ocaml/core_kernel/flags
%{_libdir}/ocaml/core_kernel/flags/*.cma
%dir %{_libdir}/ocaml/core_kernel/force_once
%{_libdir}/ocaml/core_kernel/force_once/*.cma
%dir %{_libdir}/ocaml/core_kernel/hash_heap
%{_libdir}/ocaml/core_kernel/hash_heap/*.cma
%dir %{_libdir}/ocaml/core_kernel/int_set
%{_libdir}/ocaml/core_kernel/int_set/*.cma
%dir %{_libdir}/ocaml/core_kernel/iobuf
%{_libdir}/ocaml/core_kernel/iobuf/*.cma
%dir %{_libdir}/ocaml/core_kernel/limiter
%{_libdir}/ocaml/core_kernel/limiter/*.cma
%dir %{_libdir}/ocaml/core_kernel/linked_stack
%{_libdir}/ocaml/core_kernel/linked_stack/*.cma
%dir %{_libdir}/ocaml/core_kernel/moption
%{_libdir}/ocaml/core_kernel/moption/*.cma
%dir %{_libdir}/ocaml/core_kernel/pairing_heap
%{_libdir}/ocaml/core_kernel/pairing_heap/*.cma
%dir %{_libdir}/ocaml/core_kernel/pooled_hashtbl
%{_libdir}/ocaml/core_kernel/pooled_hashtbl/*.cma
%dir %{_libdir}/ocaml/core_kernel/rope
%{_libdir}/ocaml/core_kernel/rope/*.cma
%dir %{_libdir}/ocaml/core_kernel/sexp_hidden_in_test
%{_libdir}/ocaml/core_kernel/sexp_hidden_in_test/*.cma
%dir %{_libdir}/ocaml/core_kernel/thread_pool_cpu_affinity
%{_libdir}/ocaml/core_kernel/thread_pool_cpu_affinity/*.cma
%dir %{_libdir}/ocaml/core_kernel/thread_safe_queue
%{_libdir}/ocaml/core_kernel/thread_safe_queue/*.cma
%dir %{_libdir}/ocaml/core_kernel/timing_wheel
%{_libdir}/ocaml/core_kernel/timing_wheel/*.cma
%dir %{_libdir}/ocaml/core_kernel/total_map
%{_libdir}/ocaml/core_kernel/total_map/*.cma
%dir %{_libdir}/ocaml/core_kernel/tuple_pool
%{_libdir}/ocaml/core_kernel/tuple_pool/*.cma
%dir %{_libdir}/ocaml/core_kernel/univ
%{_libdir}/ocaml/core_kernel/univ/*.cma
%dir %{_libdir}/ocaml/core_kernel/unpack_buffer
%{_libdir}/ocaml/core_kernel/unpack_buffer/*.cma
%dir %{_libdir}/ocaml/core_kernel/uopt
%{_libdir}/ocaml/core_kernel/uopt/*.cma
%dir %{_libdir}/ocaml/core_kernel/uuid
%{_libdir}/ocaml/core_kernel/uuid/*.cma
%dir %{_libdir}/ocaml/core_kernel/version_util
%{_libdir}/ocaml/core_kernel/version_util/version_util.js
%{_libdir}/ocaml/core_kernel/version_util/*.cma
%dir %{_libdir}/ocaml/core_kernel/weak_array
%{_libdir}/ocaml/core_kernel/weak_array/*.cma
%dir %{_libdir}/ocaml/core_kernel/weak_hashtbl
%{_libdir}/ocaml/core_kernel/weak_hashtbl/*.cma
%dir %{_libdir}/ocaml/core_kernel/weak_pointer
%{_libdir}/ocaml/core_kernel/weak_pointer/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/ansi_kernel/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/balanced_reducer/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/base_for_tests/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/binary_packing/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/bounded_int_table/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/bus/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/caml_unix/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/composition_infix/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/enum/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/fheap/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/flags/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/force_once/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/hash_heap/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/int_set/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/iobuf/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/limiter/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/linked_stack/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/moption/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/pairing_heap/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/pooled_hashtbl/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/rope/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/sexp_hidden_in_test/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/thread_pool_cpu_affinity/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/thread_safe_queue/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/timing_wheel/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/total_map/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/tuple_pool/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/univ/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/unpack_buffer/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/uopt/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/uuid/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/version_util/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/weak_array/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/weak_hashtbl/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core_kernel/weak_pointer/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllcore_kernel_stubs.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllversion_util_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/core_kernel/libcore_kernel_stubs.a
%{_libdir}/ocaml/core_kernel/time_ns_stubs.h
%{_libdir}/ocaml/core_kernel/*.cmi
%{_libdir}/ocaml/core_kernel/*.cmt
%{_libdir}/ocaml/core_kernel/*.cmti
%{_libdir}/ocaml/core_kernel/*.mli
%{_libdir}/ocaml/core_kernel/ansi_kernel/*.cmi
%{_libdir}/ocaml/core_kernel/ansi_kernel/*.cmt
%{_libdir}/ocaml/core_kernel/ansi_kernel/*.cmti
%{_libdir}/ocaml/core_kernel/ansi_kernel/*.mli
%{_libdir}/ocaml/core_kernel/balanced_reducer/*.cmi
%{_libdir}/ocaml/core_kernel/balanced_reducer/*.cmt
%{_libdir}/ocaml/core_kernel/balanced_reducer/*.cmti
%{_libdir}/ocaml/core_kernel/balanced_reducer/*.mli
%{_libdir}/ocaml/core_kernel/base_for_tests/*.cmi
%{_libdir}/ocaml/core_kernel/base_for_tests/*.cmt
%{_libdir}/ocaml/core_kernel/base_for_tests/*.cmti
%{_libdir}/ocaml/core_kernel/base_for_tests/*.mli
%{_libdir}/ocaml/core_kernel/binary_packing/*.cmi
%{_libdir}/ocaml/core_kernel/binary_packing/*.cmt
%{_libdir}/ocaml/core_kernel/binary_packing/*.cmti
%{_libdir}/ocaml/core_kernel/binary_packing/*.mli
%{_libdir}/ocaml/core_kernel/bounded_int_table/*.cmi
%{_libdir}/ocaml/core_kernel/bounded_int_table/*.cmt
%{_libdir}/ocaml/core_kernel/bounded_int_table/*.cmti
%{_libdir}/ocaml/core_kernel/bounded_int_table/*.mli
%{_libdir}/ocaml/core_kernel/bus/*.cmi
%{_libdir}/ocaml/core_kernel/bus/*.cmt
%{_libdir}/ocaml/core_kernel/bus/*.cmti
%{_libdir}/ocaml/core_kernel/bus/*.mli
%{_libdir}/ocaml/core_kernel/caml_unix/*.cmi
%{_libdir}/ocaml/core_kernel/caml_unix/*.cmt
%{_libdir}/ocaml/core_kernel/composition_infix/*.cmi
%{_libdir}/ocaml/core_kernel/composition_infix/*.cmt
%{_libdir}/ocaml/core_kernel/composition_infix/*.cmti
%{_libdir}/ocaml/core_kernel/composition_infix/*.mli
%{_libdir}/ocaml/core_kernel/enum/*.cmi
%{_libdir}/ocaml/core_kernel/enum/*.cmt
%{_libdir}/ocaml/core_kernel/enum/*.cmti
%{_libdir}/ocaml/core_kernel/enum/*.mli
%{_libdir}/ocaml/core_kernel/fheap/*.cmi
%{_libdir}/ocaml/core_kernel/fheap/*.cmt
%{_libdir}/ocaml/core_kernel/fheap/*.cmti
%{_libdir}/ocaml/core_kernel/fheap/*.mli
%{_libdir}/ocaml/core_kernel/flags/*.cmi
%{_libdir}/ocaml/core_kernel/flags/*.cmt
%{_libdir}/ocaml/core_kernel/flags/*.cmti
%{_libdir}/ocaml/core_kernel/flags/*.mli
%{_libdir}/ocaml/core_kernel/force_once/*.cmi
%{_libdir}/ocaml/core_kernel/force_once/*.cmt
%{_libdir}/ocaml/core_kernel/force_once/*.cmti
%{_libdir}/ocaml/core_kernel/force_once/*.mli
%{_libdir}/ocaml/core_kernel/hash_heap/*.cmi
%{_libdir}/ocaml/core_kernel/hash_heap/*.cmt
%{_libdir}/ocaml/core_kernel/hash_heap/*.cmti
%{_libdir}/ocaml/core_kernel/hash_heap/*.mli
%{_libdir}/ocaml/core_kernel/int_set/*.cmi
%{_libdir}/ocaml/core_kernel/int_set/*.cmt
%{_libdir}/ocaml/core_kernel/int_set/*.cmti
%{_libdir}/ocaml/core_kernel/int_set/*.mli
%{_libdir}/ocaml/core_kernel/iobuf/*.cmi
%{_libdir}/ocaml/core_kernel/iobuf/*.cmt
%{_libdir}/ocaml/core_kernel/iobuf/*.cmti
%{_libdir}/ocaml/core_kernel/iobuf/*.mli
%{_libdir}/ocaml/core_kernel/limiter/*.cmi
%{_libdir}/ocaml/core_kernel/limiter/*.cmt
%{_libdir}/ocaml/core_kernel/limiter/*.cmti
%{_libdir}/ocaml/core_kernel/limiter/*.mli
%{_libdir}/ocaml/core_kernel/linked_stack/*.cmi
%{_libdir}/ocaml/core_kernel/linked_stack/*.cmt
%{_libdir}/ocaml/core_kernel/linked_stack/*.cmti
%{_libdir}/ocaml/core_kernel/linked_stack/*.mli
%{_libdir}/ocaml/core_kernel/moption/*.cmi
%{_libdir}/ocaml/core_kernel/moption/*.cmt
%{_libdir}/ocaml/core_kernel/moption/*.cmti
%{_libdir}/ocaml/core_kernel/moption/*.mli
%{_libdir}/ocaml/core_kernel/pairing_heap/*.cmi
%{_libdir}/ocaml/core_kernel/pairing_heap/*.cmt
%{_libdir}/ocaml/core_kernel/pairing_heap/*.cmti
%{_libdir}/ocaml/core_kernel/pairing_heap/*.mli
%{_libdir}/ocaml/core_kernel/pooled_hashtbl/*.cmi
%{_libdir}/ocaml/core_kernel/pooled_hashtbl/*.cmt
%{_libdir}/ocaml/core_kernel/pooled_hashtbl/*.cmti
%{_libdir}/ocaml/core_kernel/pooled_hashtbl/*.mli
%{_libdir}/ocaml/core_kernel/rope/*.cmi
%{_libdir}/ocaml/core_kernel/rope/*.cmt
%{_libdir}/ocaml/core_kernel/rope/*.cmti
%{_libdir}/ocaml/core_kernel/rope/*.mli
%{_libdir}/ocaml/core_kernel/sexp_hidden_in_test/*.cmi
%{_libdir}/ocaml/core_kernel/sexp_hidden_in_test/*.cmt
%{_libdir}/ocaml/core_kernel/sexp_hidden_in_test/*.cmti
%{_libdir}/ocaml/core_kernel/sexp_hidden_in_test/*.mli
%{_libdir}/ocaml/core_kernel/thread_pool_cpu_affinity/*.cmi
%{_libdir}/ocaml/core_kernel/thread_pool_cpu_affinity/*.cmt
%{_libdir}/ocaml/core_kernel/thread_pool_cpu_affinity/*.cmti
%{_libdir}/ocaml/core_kernel/thread_pool_cpu_affinity/*.mli
%{_libdir}/ocaml/core_kernel/thread_safe_queue/*.cmi
%{_libdir}/ocaml/core_kernel/thread_safe_queue/*.cmt
%{_libdir}/ocaml/core_kernel/thread_safe_queue/*.cmti
%{_libdir}/ocaml/core_kernel/thread_safe_queue/*.mli
%{_libdir}/ocaml/core_kernel/timing_wheel/*.cmi
%{_libdir}/ocaml/core_kernel/timing_wheel/*.cmt
%{_libdir}/ocaml/core_kernel/timing_wheel/*.cmti
%{_libdir}/ocaml/core_kernel/timing_wheel/*.mli
%{_libdir}/ocaml/core_kernel/total_map/*.cmi
%{_libdir}/ocaml/core_kernel/total_map/*.cmt
%{_libdir}/ocaml/core_kernel/total_map/*.cmti
%{_libdir}/ocaml/core_kernel/total_map/*.mli
%{_libdir}/ocaml/core_kernel/tuple_pool/*.cmi
%{_libdir}/ocaml/core_kernel/tuple_pool/*.cmt
%{_libdir}/ocaml/core_kernel/tuple_pool/*.cmti
%{_libdir}/ocaml/core_kernel/tuple_pool/*.mli
%{_libdir}/ocaml/core_kernel/univ/*.cmi
%{_libdir}/ocaml/core_kernel/univ/*.cmt
%{_libdir}/ocaml/core_kernel/univ/*.cmti
%{_libdir}/ocaml/core_kernel/univ/*.mli
%{_libdir}/ocaml/core_kernel/unpack_buffer/*.cmi
%{_libdir}/ocaml/core_kernel/unpack_buffer/*.cmt
%{_libdir}/ocaml/core_kernel/unpack_buffer/*.cmti
%{_libdir}/ocaml/core_kernel/unpack_buffer/*.mli
%{_libdir}/ocaml/core_kernel/uopt/*.cmi
%{_libdir}/ocaml/core_kernel/uopt/*.cmt
%{_libdir}/ocaml/core_kernel/uopt/*.cmti
%{_libdir}/ocaml/core_kernel/uopt/*.mli
%{_libdir}/ocaml/core_kernel/uuid/*.cmi
%{_libdir}/ocaml/core_kernel/uuid/*.cmt
%{_libdir}/ocaml/core_kernel/uuid/*.cmti
%{_libdir}/ocaml/core_kernel/uuid/*.mli
%{_libdir}/ocaml/core_kernel/version_util/libversion_util_stubs.a
%{_libdir}/ocaml/core_kernel/version_util/*.cmi
%{_libdir}/ocaml/core_kernel/version_util/*.cmt
%{_libdir}/ocaml/core_kernel/version_util/*.cmti
%{_libdir}/ocaml/core_kernel/version_util/*.mli
%{_libdir}/ocaml/core_kernel/weak_array/*.cmi
%{_libdir}/ocaml/core_kernel/weak_array/*.cmt
%{_libdir}/ocaml/core_kernel/weak_array/*.cmti
%{_libdir}/ocaml/core_kernel/weak_array/*.mli
%{_libdir}/ocaml/core_kernel/weak_hashtbl/*.cmi
%{_libdir}/ocaml/core_kernel/weak_hashtbl/*.cmt
%{_libdir}/ocaml/core_kernel/weak_hashtbl/*.cmti
%{_libdir}/ocaml/core_kernel/weak_hashtbl/*.mli
%{_libdir}/ocaml/core_kernel/weak_pointer/*.cmi
%{_libdir}/ocaml/core_kernel/weak_pointer/*.cmt
%{_libdir}/ocaml/core_kernel/weak_pointer/*.cmti
%{_libdir}/ocaml/core_kernel/weak_pointer/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/core_kernel/core_kernel.a
%{_libdir}/ocaml/core_kernel/*.cmx
%{_libdir}/ocaml/core_kernel/*.cmxa
%{_libdir}/ocaml/core_kernel/ansi_kernel/ansi_kernel.a
%{_libdir}/ocaml/core_kernel/ansi_kernel/*.cmx
%{_libdir}/ocaml/core_kernel/ansi_kernel/*.cmxa
%{_libdir}/ocaml/core_kernel/balanced_reducer/balanced_reducer.a
%{_libdir}/ocaml/core_kernel/balanced_reducer/*.cmx
%{_libdir}/ocaml/core_kernel/balanced_reducer/*.cmxa
%{_libdir}/ocaml/core_kernel/base_for_tests/base_for_tests.a
%{_libdir}/ocaml/core_kernel/base_for_tests/*.cmx
%{_libdir}/ocaml/core_kernel/base_for_tests/*.cmxa
%{_libdir}/ocaml/core_kernel/binary_packing/binary_packing.a
%{_libdir}/ocaml/core_kernel/binary_packing/*.cmx
%{_libdir}/ocaml/core_kernel/binary_packing/*.cmxa
%{_libdir}/ocaml/core_kernel/bounded_int_table/bounded_int_table.a
%{_libdir}/ocaml/core_kernel/bounded_int_table/*.cmx
%{_libdir}/ocaml/core_kernel/bounded_int_table/*.cmxa
%{_libdir}/ocaml/core_kernel/bus/bus.a
%{_libdir}/ocaml/core_kernel/bus/*.cmx
%{_libdir}/ocaml/core_kernel/bus/*.cmxa
%{_libdir}/ocaml/core_kernel/caml_unix/caml_unix.a
%{_libdir}/ocaml/core_kernel/caml_unix/*.cmx
%{_libdir}/ocaml/core_kernel/caml_unix/*.cmxa
%{_libdir}/ocaml/core_kernel/composition_infix/composition_infix.a
%{_libdir}/ocaml/core_kernel/composition_infix/*.cmx
%{_libdir}/ocaml/core_kernel/composition_infix/*.cmxa
%{_libdir}/ocaml/core_kernel/enum/enum.a
%{_libdir}/ocaml/core_kernel/enum/*.cmx
%{_libdir}/ocaml/core_kernel/enum/*.cmxa
%{_libdir}/ocaml/core_kernel/fheap/fheap.a
%{_libdir}/ocaml/core_kernel/fheap/*.cmx
%{_libdir}/ocaml/core_kernel/fheap/*.cmxa
%{_libdir}/ocaml/core_kernel/flags/flags.a
%{_libdir}/ocaml/core_kernel/flags/*.cmx
%{_libdir}/ocaml/core_kernel/flags/*.cmxa
%{_libdir}/ocaml/core_kernel/force_once/force_once.a
%{_libdir}/ocaml/core_kernel/force_once/*.cmx
%{_libdir}/ocaml/core_kernel/force_once/*.cmxa
%{_libdir}/ocaml/core_kernel/hash_heap/hash_heap.a
%{_libdir}/ocaml/core_kernel/hash_heap/*.cmx
%{_libdir}/ocaml/core_kernel/hash_heap/*.cmxa
%{_libdir}/ocaml/core_kernel/int_set/int_set.a
%{_libdir}/ocaml/core_kernel/int_set/*.cmx
%{_libdir}/ocaml/core_kernel/int_set/*.cmxa
%{_libdir}/ocaml/core_kernel/iobuf/iobuf.a
%{_libdir}/ocaml/core_kernel/iobuf/*.cmx
%{_libdir}/ocaml/core_kernel/iobuf/*.cmxa
%{_libdir}/ocaml/core_kernel/limiter/limiter.a
%{_libdir}/ocaml/core_kernel/limiter/*.cmx
%{_libdir}/ocaml/core_kernel/limiter/*.cmxa
%{_libdir}/ocaml/core_kernel/linked_stack/linked_stack.a
%{_libdir}/ocaml/core_kernel/linked_stack/*.cmx
%{_libdir}/ocaml/core_kernel/linked_stack/*.cmxa
%{_libdir}/ocaml/core_kernel/moption/moption.a
%{_libdir}/ocaml/core_kernel/moption/*.cmx
%{_libdir}/ocaml/core_kernel/moption/*.cmxa
%{_libdir}/ocaml/core_kernel/pairing_heap/pairing_heap.a
%{_libdir}/ocaml/core_kernel/pairing_heap/*.cmx
%{_libdir}/ocaml/core_kernel/pairing_heap/*.cmxa
%{_libdir}/ocaml/core_kernel/pooled_hashtbl/pooled_hashtbl.a
%{_libdir}/ocaml/core_kernel/pooled_hashtbl/*.cmx
%{_libdir}/ocaml/core_kernel/pooled_hashtbl/*.cmxa
%{_libdir}/ocaml/core_kernel/rope/rope.a
%{_libdir}/ocaml/core_kernel/rope/*.cmx
%{_libdir}/ocaml/core_kernel/rope/*.cmxa
%{_libdir}/ocaml/core_kernel/sexp_hidden_in_test/sexp_hidden_in_test.a
%{_libdir}/ocaml/core_kernel/sexp_hidden_in_test/*.cmx
%{_libdir}/ocaml/core_kernel/sexp_hidden_in_test/*.cmxa
%{_libdir}/ocaml/core_kernel/thread_pool_cpu_affinity/thread_pool_cpu_affinity.a
%{_libdir}/ocaml/core_kernel/thread_pool_cpu_affinity/*.cmx
%{_libdir}/ocaml/core_kernel/thread_pool_cpu_affinity/*.cmxa
%{_libdir}/ocaml/core_kernel/thread_safe_queue/thread_safe_queue.a
%{_libdir}/ocaml/core_kernel/thread_safe_queue/*.cmx
%{_libdir}/ocaml/core_kernel/thread_safe_queue/*.cmxa
%{_libdir}/ocaml/core_kernel/timing_wheel/timing_wheel.a
%{_libdir}/ocaml/core_kernel/timing_wheel/*.cmx
%{_libdir}/ocaml/core_kernel/timing_wheel/*.cmxa
%{_libdir}/ocaml/core_kernel/total_map/total_map.a
%{_libdir}/ocaml/core_kernel/total_map/*.cmx
%{_libdir}/ocaml/core_kernel/total_map/*.cmxa
%{_libdir}/ocaml/core_kernel/tuple_pool/tuple_pool.a
%{_libdir}/ocaml/core_kernel/tuple_pool/*.cmx
%{_libdir}/ocaml/core_kernel/tuple_pool/*.cmxa
%{_libdir}/ocaml/core_kernel/univ/univ.a
%{_libdir}/ocaml/core_kernel/univ/*.cmx
%{_libdir}/ocaml/core_kernel/univ/*.cmxa
%{_libdir}/ocaml/core_kernel/unpack_buffer/unpack_buffer.a
%{_libdir}/ocaml/core_kernel/unpack_buffer/*.cmx
%{_libdir}/ocaml/core_kernel/unpack_buffer/*.cmxa
%{_libdir}/ocaml/core_kernel/uopt/uopt.a
%{_libdir}/ocaml/core_kernel/uopt/*.cmx
%{_libdir}/ocaml/core_kernel/uopt/*.cmxa
%{_libdir}/ocaml/core_kernel/uuid/uuid.a
%{_libdir}/ocaml/core_kernel/uuid/*.cmx
%{_libdir}/ocaml/core_kernel/uuid/*.cmxa
%{_libdir}/ocaml/core_kernel/version_util/version_util.a
%{_libdir}/ocaml/core_kernel/version_util/*.cmx
%{_libdir}/ocaml/core_kernel/version_util/*.cmxa
%{_libdir}/ocaml/core_kernel/weak_array/weak_array.a
%{_libdir}/ocaml/core_kernel/weak_array/*.cmx
%{_libdir}/ocaml/core_kernel/weak_array/*.cmxa
%{_libdir}/ocaml/core_kernel/weak_hashtbl/weak_hashtbl.a
%{_libdir}/ocaml/core_kernel/weak_hashtbl/*.cmx
%{_libdir}/ocaml/core_kernel/weak_hashtbl/*.cmxa
%{_libdir}/ocaml/core_kernel/weak_pointer/weak_pointer.a
%{_libdir}/ocaml/core_kernel/weak_pointer/*.cmx
%{_libdir}/ocaml/core_kernel/weak_pointer/*.cmxa
%endif
%{_libdir}/ocaml/core_kernel/dune-package
%{_libdir}/ocaml/core_kernel/opam
