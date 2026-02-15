URLS = {
    "kde": "https://bugs.kde.org/rest/bug",
    "gentoo": "https://bugs.gentoo.org/rest/bug",
    "suse": "https://bugzilla.suse.com/rest/bug"
}

END_DATE = "2011-12-31"

LIMIT = 100
WAIT_TIME = 2

FIELDS = [
    "id",
    "creation_time",
    "last_change_time",
    "status",
    "resolution",
    "severity",
    "priority",
    "creator",
    "assigned_to",
    "comment_count",
    "dupe_of"
]