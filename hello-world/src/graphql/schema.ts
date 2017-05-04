//  This file was automatically generated and should not be edited.
/* tslint:disable */

export interface AddUserMutationVariables {
  firstName: string;
  lastName: string;
}

export interface AddUserMutation {
  addUser: {
    user: {
      firstName: string,
      lastName: string,
      emails: Array< {
        address: string,
        verified: boolean,
      } > | null,
    } | null,
  } | null;
}

export interface UsersQueryVariables {
  first_name: string | null;
}

export interface UsersQuery {
  users: {
    edges: Array< {
      // The item at the end of the edge
      node: {
        firstName: string,
        lastName: string,
        emails: Array< {
          address: string,
          verified: boolean,
        } > | null,
      } | null,
    } >,
  } | null;
}
/* tslint:enable */
