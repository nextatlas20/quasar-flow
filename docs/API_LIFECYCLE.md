# API Lifecycle Policy

Quasar Flow keeps every public symbol available for at least two minor releases
after it is marked deprecated. This file is the published record of that
promise for the 2.x line.

## API surface

### 🧬 Deprecation Register

The register mirrors the deprecation decorators shipped on this branch. Rows are
ordered by module and then by symbol. `Remove in` is the first minor release in
which the symbol may disappear; `—` in the Replacement column means there is no
drop-in substitute.

| Module | Symbol | Remove in | Replacement | Status |
| --- | --- | --- | --- | --- |
| quasar.clients.graphql | GraphQLLegacyTransport | 2.5 | GraphQLTransport | tracked |
| quasar.clients.http | LegacySession | 2.5 | HttpClient | migrating |
| quasar.clients.http | encode_query | 2.4 | urlencode_params | tracked |
| quasar.clients.http | open_legacy | 2.5 | HttpClient.request | tracked |
| quasar.core.config | load_env_config | 2.5 | ConfigLoader.from_env | migrating |
| quasar.core.pagination | page_walk | 2.7 | Paginator | tracked |
| quasar.core.retry | LegacyBackoff | 2.5 | ExponentialBackoff | waived |
| quasar.core.retry | retry_forever | 2.4 | RetryPolicy | tracked |
| quasar.streams.buffers | RingBufferV1 | 3.0 | RingBuffer | migrating |
| quasar.streams.buffers | flush_all | 2.4 | — | waived |
| quasar.streams.window | WindowAggregatorSimple | 2.6 | WindowAggregator | tracked |
| quasar.utils.serialization | dumps_pickle | 2.6 | dumps_msgpack | migrating |
| quasar.utils.timeparse | parse_iso | 2.5 | parse_timestamp | tracked |

### Removal procedure

1. Announce the removal in the release notes one minor release ahead.
2. Keep the shim importable until the release named in `Remove in`.
3. Delete the row from this register in the same commit that removes the symbol.

## Support

Questions about the policy go to #quasar-api. Security reports go to
security@quasar.example.
