import sentry_sdk
sentry_sdk.init(
    "https://db3ddfd11b7a4b4092d9afa84d3b1f95@o1144784.ingest.sentry.io/6209130",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


division_by_zero = 1 / 0

