"""Shared constants for the scripts/ directory."""

# GitHub URL path segments that are NOT owners — they're platform paths.
# Both discover_tools.py and gen_catalog_owners.py must skip these so a
# github.com/sponsors/... URL never gets misread as a trusted author.
SKIP_OWNERS = frozenset({
    "sponsors", "topics", "search", "about", "features", "marketplace",
    "collections", "orgs", "settings", "notifications",
    "repos", "org",
})
