import * as shopkeeper from "@pulumi/shopkeeper";

const page = new shopkeeper.StaticPage("page", {
    indexContent: "<html><body><p>Hello world!</p></body></html>",
});

export const bucket = page.bucket;
export const url = page.websiteUrl;
