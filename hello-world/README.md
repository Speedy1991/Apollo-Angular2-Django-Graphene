What is this
----
This is a copy from the [Hello World Example](https://github.com/apollographql/apollo-angular/tree/master/examples/hello-world)
slightly modified to work with Django Graphene


## How to run

Simply:

```
npm start
```

## Generate types

We use [`apollo-codegen`](https://github.com/apollographql/apollo-codegen) to generate types for TypeScript.

The whole idea is to hit the server to get the schema from a GraphQL endpoint for defined queries (thanks to introspection) and then turn it into TypeScript code.

You can achieve the first goal by running two commands:

```
npm run server
npm run schema:download
```

It saves informations to a file (`schema.json`) that will be used to generate types:

```
npm run schema:generate
```

So now on you have a file (`src/graphql/schema.ts`) with everything you need to combine the TypeScript's experience with GraphQL's.
