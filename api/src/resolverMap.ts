// resolverMap.ts
import { IResolvers } from 'graphql-tools';

const resolverMap: IResolvers = {
  Query: {
    helloWorld(_: void, args: void): string {
  return `👋 Hello world! 👋`;
    },
  },
  Mutation: {
    createUser: async (_: void, args: any, context: any) => {
      const data = await context.dataSources.arnApi.createUser(args.input);

      return data;
    },
    login: async (_: void, args: any, context: any) => {
      const data = await context.dataSources.arnApi.login(args.input);

      return data;
    },
    refreshToken: async (_: void, args: any, context: any) => {
      const data = await context.dataSources.arnApi.refreshToken(args.refresh);

      return data;
    }
  }
};

export default resolverMap;