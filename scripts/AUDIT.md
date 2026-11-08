# Completeness audit brief

Site content: `docs/**/*.md` (French, built from scanned manuals).
Page images: /home/manu/.cache/claude-tmp/claude-1000/-home-manu--claude-spares-spare-ViAxgM/81439095-ce99-467b-bfcc-2d5dcec62d2a/scratchpad/pages/<doc>/p-NN.jpg

For EVERY assigned page: Read the image, then grep `docs/` for its facts.
Look for technical information present on the scan but absent from the
site: values, units, ranges, defaults, parameter rows, table rows, fault
codes/causes/remedies, terminal names, wire colours, procedure steps,
warnings, figure legends, notes, footnotes. Ignore covers, TOCs,
headers/footers, distributor ads, pure duplicates of content already on
the site in other words, and the "Réglé/Modifié" blank columns.

Also flag wrong values (site differs from scan).

Do NOT edit docs/. Write findings to `staging/audit-<doc>.md`, one entry
per gap:

    ## <doc> p. N — <short label>
    Page cible : docs/<path>.md, après la section « <heading> »
    Type : manquant | erroné
    <exact French Markdown to insert, or the correction old → new>

If a page has no gap, write nothing for it. End the file with a line
`Pages auditées : <list>`. Report back a count of gaps and the 3 most
important.
