# PexelsQueryResults
This document contains information on the `PexelsQueryResults` dataclass.

# Attributes
## `content`
A list of `PexelsPhoto`, `PexelsVideo`, or `PexelsCollection` objects returned from the query.

## `url`
A URL to the targeted endpoint of the query. In the next version, all of them will also contain the added parameters, as some returned
`PexelsQueryResults` objects don't contain the full URL.

## `total_results`
The amount of results returned from the query.

## `page`
The page number of the query.

## `per_page`
How many results were supposed to be retrieved from the page (of the query).
