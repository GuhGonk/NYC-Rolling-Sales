CREATE TABLE "rolling_sales"(
    "BOROUGH" SMALLINT NOT NULL,
    "NEIGHBORHOOD" VARCHAR(255) NOT NULL,
    "BUILDING CLASS CATEGORY" VARCHAR(255) NOT NULL,
    "TAX CLASS AT PRESENT" VARCHAR(255) NOT NULL,
    "BLOCK" SMALLINT NOT NULL,
    "LOT" SMALLINT NOT NULL,
    "EASE-MENT" VARCHAR(255) NOT NULL,
    "BUILDING CLASS AT PRESENT" VARCHAR(255) NOT NULL,
    "ADDRESS" VARCHAR(255) NOT NULL,
    "APARTMENT NUMBER" VARCHAR(255) NOT NULL,
    "ZIP CODE" SMALLINT NOT NULL,
    "RESIDENTIAL UNITS" SMALLINT NOT NULL,
    "COMMERCIAL UNITS" SMALLINT NOT NULL,
    "TOTAL UNITS" SMALLINT NOT NULL,
    "LAND SQUARE FEET" SMALLINT NOT NULL,
    "GROSS SQUARE FEET" SMALLINT NOT NULL,
    "TAX CLASS AT TIME OF SALE" SMALLINT NOT NULL,
    "BUILDING CLASS AT TIME OF SALE" VARCHAR(255) NOT NULL,
    "SALE PRICE" INTEGER NOT NULL,
    "SALE DATE" DATE NOT NULL
);