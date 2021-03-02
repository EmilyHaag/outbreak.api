from .lineage import LineageByCountryHandler, LineageByDivisionHandler, LineageAndCountryHandler, LineageAndDivisionHandler, LineageHandler, LineageMutationsHandler, MutationDetailsHandler, MutationsByLineage
from .prevalence import PrevalenceByLocationHandler, PrevalenceByLocationAndTimeHandler, PrevalenceHandler, PrevalenceAllLineagesByLocationHandler, PrevalenceByAAPositionHandler
from .general import MostRecentCollectionDate, CountryHandler, DivisionHandler, MetadataHandler, MostRecentSubmissionDate, MutationHandler, SubmissionLagHandler, SequenceCountHandler

routes = [
    (r"/genomics/lineage-by-country", LineageByCountryHandler),
    (r"/genomics/lineage-by-division", LineageByDivisionHandler),
    (r"/genomics/lineage-and-country", LineageAndCountryHandler),
    (r"/genomics/lineage-and-division", LineageAndDivisionHandler),
    (r"/genomics/sequence-count", SequenceCountHandler),
    (r"/genomics/prevalence-by-location", PrevalenceByLocationHandler),
    (r"/genomics/prevalence-by-country-all-lineages", PrevalenceAllLineagesByLocationHandler),
    (r"/genomics/prevalence-by-division-all-lineages", PrevalenceAllLineagesByLocationHandler),
    (r"/genomics/prevalence-by-county-all-lineages", PrevalenceAllLineagesByLocationHandler),
    (r"/genomics/prevalence-by-position", PrevalenceByAAPositionHandler),
    (r"/genomics/global-prevalence", PrevalenceHandler),
    (r"/genomics/lineage-by-country-most-recent", PrevalenceByLocationAndTimeHandler),
    (r"/genomics/lineage-by-division-most-recent", PrevalenceByLocationAndTimeHandler),
    (r"/genomics/most-recent-collection-date", MostRecentCollectionDate),
    (r"/genomics/most-recent-submission-date", MostRecentSubmissionDate),
    (r"/genomics/mutation-details", MutationDetailsHandler),
    (r"/genomics/mutations-by-lineage", MutationsByLineage),
    (r"/genomics/lineage-mutations", LineageMutationsHandler),
    (r"/genomics/collection-submission", SubmissionLagHandler),
    (r"/genomics/country", CountryHandler),
    (r"/genomics/lineage", LineageHandler),
    (r"/genomics/division", DivisionHandler),
    (r"/genomics/mutations", MutationHandler),
    (r"/genomics/metadata", MetadataHandler)
]
