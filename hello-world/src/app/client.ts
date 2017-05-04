import { ApolloClient, createNetworkInterface } from 'apollo-client';

const client = new ApolloClient({
  networkInterface: createNetworkInterface({
    uri: 'http://localhost:8000/api/',
    opts: {
      credentials: 'same-origin',
    },
  }),
});

export function getClient(): ApolloClient {
  return client;
}
