---
section: terms
lang: ja
title: de-identification
---

非識別化 (非特定化)。[anonymisation](/glossary/ja/terms/anonymisation/) の一種で、パーソナルデータベースのレコードは保持したまま、氏名等の特定の識別情報を、匿名化された {identifiers} に置き換えること。{aggregation} と比べると、非識別化の方が [data leakage](/glossary/ja/terms/data-leakage/) のリスクが高い。for example, if prison records include a prisoner's criminal record and medical history, the prisoner could in many cases be identified even without their name by their criminal record, giving unauthorised access to their medical history. In other cases this risk is absent, or the value of the un-aggregated data is so great that it is worth making de-identified data available subject to carefully designed safeguards.

A form of [anonymisation](/glossary/en/terms/anonymisation/) where personal records are kept intact but specific identifying information, such as names, are replaced with anonymous {identifiers}. Compared to {aggregation}, de-identification carries a greater risk of [data leakage](/glossary/en/terms/data-leakage/): for example, if prison records include a prisoner's criminal record and medical history, the prisoner could in many cases be identified even without their name by their criminal record, giving unauthorised access to their medical history. In other cases this risk is absent, or the value of the un-aggregated data is so great that it is worth making de-identified data available subject to carefully designed safeguards.
