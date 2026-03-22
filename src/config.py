URLS = {
    "kde": "https://bugs.kde.org/rest/bug",
    "gentoo": "https://bugs.gentoo.org/rest/bug",
    "suse": "https://bugzilla.suse.com/rest/bug"
}

LIMIT = 200

FIELDS = [
    "id",
    "creation_time",
    "last_change_time",
    "status",
    "resolution",
    "product",
    "component",
    "creator",
    "assigned_to",
    "priority",
    "severity",
    "dupe_of"
]