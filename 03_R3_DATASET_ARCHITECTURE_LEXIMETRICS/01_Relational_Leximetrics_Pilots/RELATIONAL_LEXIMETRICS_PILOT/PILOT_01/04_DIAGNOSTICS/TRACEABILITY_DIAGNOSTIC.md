# Traceability diagnostic

Traceability improves materially when the relationship row stores a provision reference, an official CELEX URL, an existing dataset record ID, and an evidence link. In this pilot, P01 and P04 have article references in the current workbook narrative; P02, P03 and P05 do not have a structured provision reference in the coding sheet, even though their narratives describe detailed legal work.

Accordingly, evidence is classified as `NORMALIZED_DATASET_STATEMENT` unless a direct source excerpt is present. The pilot does not convert normalized narrative into a verbatim quotation. Rows with missing provision references carry explicit issue flags and are not treated as fully source-verified.

This supports the value of provision anchoring while also showing the cost: source retrieval and article-level validation are prerequisites before scaling.
