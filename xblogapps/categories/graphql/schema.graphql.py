type CategoryType {
    id: ID!,
    name: String!,
    slug: String,
    description: String,
    threads: [ThreadType]
}

input CategoryCreateInput {
    id: ID,
    name: String,
    description: String,
    slug: String,
}

input CategoryEditPatchInput {
    name: String,
    description: String,
    slug: String,
}

input CategoryEditInput {
    id: Int,
    slug: String,
    patch: CategoryEditPatchInput
}

input CategoryDeleteInput {
    id: Int,
    slug: String
}

type CategoryCreatePayload {
    category: Category
}

type CategoryDeletePayload {
    category: [CategoryType]
}

type CategoryEditPayload {
    category: Category
}

type Mutation {
    categoryCreate (input: CategoryCreateInput): CategoryCreatePayload,
    categoryDelete (input: CategoryDeleteInput): CategoryDeletePayload,
    categoryEdit (input: CategoryEditInput): CategoryEditPayload,
}

type Query {
    getAllCategories() categories: [CategoryType],
    getCategoryByIdAndSlug(id: ID!, slug: String!) category(id, slug): CategoryType!
}

schema {
    query: Query,
    mutation: Mutation,
}