#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : claws-mail
Version  : 3.15.0
Release  : 3
URL      : http://www.claws-mail.org/download.php?file=releases/claws-mail-3.15.0.tar.gz
Source0  : http://www.claws-mail.org/download.php?file=releases/claws-mail-3.15.0.tar.gz
Summary  : Claws Mail
Group    : Development/Tools
License  : GPL-3.0
Requires: claws-mail-bin
Requires: claws-mail-lib
Requires: claws-mail-data
Requires: claws-mail-doc
Requires: claws-mail-locales
BuildRequires : bison
BuildRequires : dbus-dev
BuildRequires : flex
BuildRequires : gettext
BuildRequires : openldap-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libcanberra-gtk)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libical)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libsoup-gnome-2.4)
BuildRequires : pkgconfig(libstartup-notification-1.0)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(valgrind)

%description
Claws Mail - a GTK+ based, lightweight, and fast e-mail client
---------------------------------------------------------------------

%package bin
Summary: bin components for the claws-mail package.
Group: Binaries
Requires: claws-mail-data

%description bin
bin components for the claws-mail package.


%package data
Summary: data components for the claws-mail package.
Group: Data

%description data
data components for the claws-mail package.


%package dev
Summary: dev components for the claws-mail package.
Group: Development
Requires: claws-mail-lib
Requires: claws-mail-bin
Requires: claws-mail-data
Provides: claws-mail-devel

%description dev
dev components for the claws-mail package.


%package doc
Summary: doc components for the claws-mail package.
Group: Documentation

%description doc
doc components for the claws-mail package.


%package lib
Summary: lib components for the claws-mail package.
Group: Libraries
Requires: claws-mail-data

%description lib
lib components for the claws-mail package.


%package locales
Summary: locales components for the claws-mail package.
Group: Default

%description locales
locales components for the claws-mail package.


%prep
%setup -q -n claws-mail-3.15.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490541552
%configure --disable-static --disable-libetpan
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1490541552
rm -rf %{buildroot}
%make_install
%find_lang claws-mail

%files
%defattr(-,root,root,-)
/usr/lib64/claws-mail/plugins/pgpinline.deps
/usr/lib64/claws-mail/plugins/pgpmime.deps
/usr/lib64/claws-mail/plugins/smime.deps

%files bin
%defattr(-,root,root,-)
/usr/bin/claws-mail
/usr/bin/sylpheed-claws

%files data
%defattr(-,root,root,-)
/usr/share/applications/claws-mail.desktop
/usr/share/icons/hicolor/128x128/apps/claws-mail.png
/usr/share/icons/hicolor/48x48/apps/claws-mail.png
/usr/share/icons/hicolor/64x64/apps/claws-mail.png

%files dev
%defattr(-,root,root,-)
/usr/include/claws-mail/account.h
/usr/include/claws-mail/action.h
/usr/include/claws-mail/adbookbase.h
/usr/include/claws-mail/addr_compl.h
/usr/include/claws-mail/addrbook.h
/usr/include/claws-mail/addrcache.h
/usr/include/claws-mail/addrclip.h
/usr/include/claws-mail/addrcustomattr.h
/usr/include/claws-mail/addrdefs.h
/usr/include/claws-mail/addrduplicates.h
/usr/include/claws-mail/addressadd.h
/usr/include/claws-mail/addressbook-dbus.h
/usr/include/claws-mail/addressbook.h
/usr/include/claws-mail/addressbook_foldersel.h
/usr/include/claws-mail/addressitem.h
/usr/include/claws-mail/addrgather.h
/usr/include/claws-mail/addrharvest.h
/usr/include/claws-mail/addrindex.h
/usr/include/claws-mail/addritem.h
/usr/include/claws-mail/addrquery.h
/usr/include/claws-mail/addrselect.h
/usr/include/claws-mail/advsearch.h
/usr/include/claws-mail/alertpanel.h
/usr/include/claws-mail/autofaces.h
/usr/include/claws-mail/avatars.h
/usr/include/claws-mail/browseldap.h
/usr/include/claws-mail/claws-features.h
/usr/include/claws-mail/codeconv.h
/usr/include/claws-mail/common/claws.h
/usr/include/claws-mail/common/defs.h
/usr/include/claws-mail/common/hooks.h
/usr/include/claws-mail/common/log.h
/usr/include/claws-mail/common/md5.h
/usr/include/claws-mail/common/mgutils.h
/usr/include/claws-mail/common/passcrypt.h
/usr/include/claws-mail/common/pkcs5_pbkdf2.h
/usr/include/claws-mail/common/plugin.h
/usr/include/claws-mail/common/prefs.h
/usr/include/claws-mail/common/progressindicator.h
/usr/include/claws-mail/common/quoted-printable.h
/usr/include/claws-mail/common/session.h
/usr/include/claws-mail/common/smtp.h
/usr/include/claws-mail/common/socket.h
/usr/include/claws-mail/common/ssl.h
/usr/include/claws-mail/common/ssl_certificate.h
/usr/include/claws-mail/common/string_match.h
/usr/include/claws-mail/common/stringtable.h
/usr/include/claws-mail/common/tags.h
/usr/include/claws-mail/common/template.h
/usr/include/claws-mail/common/timing.h
/usr/include/claws-mail/common/tlds.h
/usr/include/claws-mail/common/utils.h
/usr/include/claws-mail/common/uuencode.h
/usr/include/claws-mail/common/version.h
/usr/include/claws-mail/common/xml.h
/usr/include/claws-mail/common/xmlprops.h
/usr/include/claws-mail/compose.h
/usr/include/claws-mail/crash.h
/usr/include/claws-mail/customheader.h
/usr/include/claws-mail/displayheader.h
/usr/include/claws-mail/editaddress.h
/usr/include/claws-mail/editaddress_other_attributes_ldap.h
/usr/include/claws-mail/editbook.h
/usr/include/claws-mail/editgroup.h
/usr/include/claws-mail/editjpilot.h
/usr/include/claws-mail/editldap.h
/usr/include/claws-mail/editldap_basedn.h
/usr/include/claws-mail/edittags.h
/usr/include/claws-mail/editvcard.h
/usr/include/claws-mail/enriched.h
/usr/include/claws-mail/exphtmldlg.h
/usr/include/claws-mail/expldifdlg.h
/usr/include/claws-mail/export.h
/usr/include/claws-mail/exporthtml.h
/usr/include/claws-mail/exportldif.h
/usr/include/claws-mail/file_checker.h
/usr/include/claws-mail/filtering.h
/usr/include/claws-mail/folder.h
/usr/include/claws-mail/folder_item_prefs.h
/usr/include/claws-mail/foldersel.h
/usr/include/claws-mail/folderutils.h
/usr/include/claws-mail/folderview.h
/usr/include/claws-mail/grouplistdialog.h
/usr/include/claws-mail/gtk/about.h
/usr/include/claws-mail/gtk/authors.h
/usr/include/claws-mail/gtk/claws-marshal.h
/usr/include/claws-mail/gtk/colorlabel.h
/usr/include/claws-mail/gtk/colorsel.h
/usr/include/claws-mail/gtk/combobox.h
/usr/include/claws-mail/gtk/description_window.h
/usr/include/claws-mail/gtk/filesel.h
/usr/include/claws-mail/gtk/foldersort.h
/usr/include/claws-mail/gtk/gdkkeysyms-new.h
/usr/include/claws-mail/gtk/gtkaspell.h
/usr/include/claws-mail/gtk/gtkcmclist.h
/usr/include/claws-mail/gtk/gtkcmctree.h
/usr/include/claws-mail/gtk/gtkcmoptionmenu.h
/usr/include/claws-mail/gtk/gtksctree.h
/usr/include/claws-mail/gtk/gtkshruler.h
/usr/include/claws-mail/gtk/gtkunit.h
/usr/include/claws-mail/gtk/gtkutils.h
/usr/include/claws-mail/gtk/gtkvscrollbutton.h
/usr/include/claws-mail/gtk/headers.h
/usr/include/claws-mail/gtk/icon_legend.h
/usr/include/claws-mail/gtk/inputdialog.h
/usr/include/claws-mail/gtk/logwindow.h
/usr/include/claws-mail/gtk/manage_window.h
/usr/include/claws-mail/gtk/menu.h
/usr/include/claws-mail/gtk/pluginwindow.h
/usr/include/claws-mail/gtk/prefswindow.h
/usr/include/claws-mail/gtk/progressdialog.h
/usr/include/claws-mail/gtk/quicksearch.h
/usr/include/claws-mail/gtk/spell_entry.h
/usr/include/claws-mail/gtk/sslcertwindow.h
/usr/include/claws-mail/headerview.h
/usr/include/claws-mail/html.h
/usr/include/claws-mail/image_viewer.h
/usr/include/claws-mail/imap.h
/usr/include/claws-mail/imap_gtk.h
/usr/include/claws-mail/import.h
/usr/include/claws-mail/importldif.h
/usr/include/claws-mail/importmutt.h
/usr/include/claws-mail/importpine.h
/usr/include/claws-mail/inc.h
/usr/include/claws-mail/jpilot.h
/usr/include/claws-mail/ldapctrl.h
/usr/include/claws-mail/ldaplocate.h
/usr/include/claws-mail/ldapquery.h
/usr/include/claws-mail/ldapserver.h
/usr/include/claws-mail/ldapupdate.h
/usr/include/claws-mail/ldaputil.h
/usr/include/claws-mail/ldif.h
/usr/include/claws-mail/localfolder.h
/usr/include/claws-mail/main.h
/usr/include/claws-mail/mainwindow.h
/usr/include/claws-mail/manual.h
/usr/include/claws-mail/matcher.h
/usr/include/claws-mail/matcher_parser.h
/usr/include/claws-mail/matcher_parser_lex.h
/usr/include/claws-mail/matcher_parser_parse.h
/usr/include/claws-mail/matchertypes.h
/usr/include/claws-mail/mbox.h
/usr/include/claws-mail/message_search.h
/usr/include/claws-mail/messageview.h
/usr/include/claws-mail/mh.h
/usr/include/claws-mail/mh_gtk.h
/usr/include/claws-mail/mimeview.h
/usr/include/claws-mail/msgcache.h
/usr/include/claws-mail/mutt.h
/usr/include/claws-mail/news.h
/usr/include/claws-mail/news_gtk.h
/usr/include/claws-mail/noticeview.h
/usr/include/claws-mail/partial_download.h
/usr/include/claws-mail/password.h
/usr/include/claws-mail/password_gtk.h
/usr/include/claws-mail/passwordstore.h
/usr/include/claws-mail/pine.h
/usr/include/claws-mail/plugins/claws-mail/archiver.h
/usr/include/claws-mail/plugins/claws-mail/archiver_prefs.h
/usr/include/claws-mail/plugins/claws-mail/gtkhotkey/eggaccelerators.h
/usr/include/claws-mail/plugins/claws-mail/gtkhotkey/gtk-hotkey-error.h
/usr/include/claws-mail/plugins/claws-mail/gtkhotkey/gtk-hotkey-info.h
/usr/include/claws-mail/plugins/claws-mail/gtkhotkey/gtk-hotkey-key-file-registry.h
/usr/include/claws-mail/plugins/claws-mail/gtkhotkey/gtk-hotkey-listener.h
/usr/include/claws-mail/plugins/claws-mail/gtkhotkey/gtk-hotkey-marshal.h
/usr/include/claws-mail/plugins/claws-mail/gtkhotkey/gtk-hotkey-registry.h
/usr/include/claws-mail/plugins/claws-mail/gtkhotkey/gtk-hotkey-utils.h
/usr/include/claws-mail/plugins/claws-mail/gtkhotkey/gtk-hotkey-x11-listener.h
/usr/include/claws-mail/plugins/claws-mail/gtkhotkey/gtkhotkey.h
/usr/include/claws-mail/plugins/claws-mail/gtkhotkey/tomboykeybinder.h
/usr/include/claws-mail/plugins/pgpcore/autocompletion.h
/usr/include/claws-mail/plugins/pgpcore/passphrase.h
/usr/include/claws-mail/plugins/pgpcore/pgp_utils.h
/usr/include/claws-mail/plugins/pgpcore/pgp_viewer.h
/usr/include/claws-mail/plugins/pgpcore/prefs_gpg.h
/usr/include/claws-mail/plugins/pgpcore/select-keys.h
/usr/include/claws-mail/plugins/pgpcore/sgpgme.h
/usr/include/claws-mail/plugins/pgpinline/pgpinline.h
/usr/include/claws-mail/plugins/pgpmime/pgpmime.h
/usr/include/claws-mail/plugins/smime/smime.h
/usr/include/claws-mail/plugins/vcalendar/vcal_interface.h
/usr/include/claws-mail/pop.h
/usr/include/claws-mail/prefs_account.h
/usr/include/claws-mail/prefs_actions.h
/usr/include/claws-mail/prefs_common.h
/usr/include/claws-mail/prefs_compose_writing.h
/usr/include/claws-mail/prefs_customheader.h
/usr/include/claws-mail/prefs_display_header.h
/usr/include/claws-mail/prefs_ext_prog.h
/usr/include/claws-mail/prefs_filtering.h
/usr/include/claws-mail/prefs_filtering_action.h
/usr/include/claws-mail/prefs_folder_column.h
/usr/include/claws-mail/prefs_folder_item.h
/usr/include/claws-mail/prefs_fonts.h
/usr/include/claws-mail/prefs_gtk.h
/usr/include/claws-mail/prefs_image_viewer.h
/usr/include/claws-mail/prefs_logging.h
/usr/include/claws-mail/prefs_matcher.h
/usr/include/claws-mail/prefs_message.h
/usr/include/claws-mail/prefs_migration.h
/usr/include/claws-mail/prefs_msg_colors.h
/usr/include/claws-mail/prefs_other.h
/usr/include/claws-mail/prefs_quote.h
/usr/include/claws-mail/prefs_receive.h
/usr/include/claws-mail/prefs_send.h
/usr/include/claws-mail/prefs_spelling.h
/usr/include/claws-mail/prefs_summaries.h
/usr/include/claws-mail/prefs_summary_column.h
/usr/include/claws-mail/prefs_summary_open.h
/usr/include/claws-mail/prefs_template.h
/usr/include/claws-mail/prefs_themes.h
/usr/include/claws-mail/prefs_toolbar.h
/usr/include/claws-mail/prefs_wrapping.h
/usr/include/claws-mail/printing.h
/usr/include/claws-mail/privacy.h
/usr/include/claws-mail/procheader.h
/usr/include/claws-mail/procmime.h
/usr/include/claws-mail/procmsg.h
/usr/include/claws-mail/proctypes.h
/usr/include/claws-mail/quote_fmt.h
/usr/include/claws-mail/quote_fmt_lex.h
/usr/include/claws-mail/quote_fmt_parse.h
/usr/include/claws-mail/recv.h
/usr/include/claws-mail/remotefolder.h
/usr/include/claws-mail/send_message.h
/usr/include/claws-mail/setup.h
/usr/include/claws-mail/sourcewindow.h
/usr/include/claws-mail/ssl_manager.h
/usr/include/claws-mail/statusbar.h
/usr/include/claws-mail/stock_pixmap.h
/usr/include/claws-mail/summary_search.h
/usr/include/claws-mail/summaryview.h
/usr/include/claws-mail/textview.h
/usr/include/claws-mail/toolbar.h
/usr/include/claws-mail/undo.h
/usr/include/claws-mail/unmime.h
/usr/include/claws-mail/uri_opener.h
/usr/include/claws-mail/vcard.h
/usr/include/claws-mail/viewtypes.h
/usr/include/claws-mail/wizard.h
/usr/lib64/pkgconfig/claws-mail.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/claws\-mail/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/claws-mail/plugins/acpi_notifier.so
/usr/lib64/claws-mail/plugins/address_keeper.so
/usr/lib64/claws-mail/plugins/archive.so
/usr/lib64/claws-mail/plugins/att_remover.so
/usr/lib64/claws-mail/plugins/attachwarner.so
/usr/lib64/claws-mail/plugins/bogofilter.so
/usr/lib64/claws-mail/plugins/bsfilter.so
/usr/lib64/claws-mail/plugins/clamd.so
/usr/lib64/claws-mail/plugins/fetchinfo.so
/usr/lib64/claws-mail/plugins/libravatar.so
/usr/lib64/claws-mail/plugins/mailmbox.so
/usr/lib64/claws-mail/plugins/managesieve.so
/usr/lib64/claws-mail/plugins/newmail.so
/usr/lib64/claws-mail/plugins/notification.so
/usr/lib64/claws-mail/plugins/rssyl.so
/usr/lib64/claws-mail/plugins/spamassassin.so
/usr/lib64/claws-mail/plugins/spamreport.so
/usr/lib64/claws-mail/plugins/vcalendar.so

%files locales -f claws-mail.lang
%defattr(-,root,root,-)

