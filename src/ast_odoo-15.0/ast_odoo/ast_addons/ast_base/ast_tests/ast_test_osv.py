Module(
    body=[
        ImportFrom(
            module='odoo.osv.query',
            names=[alias(name='Query', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='BaseCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='QueryTestCase',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_basic_query',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Name(id='Query', ctx=Load()),
                                args=[
                                    Constant(value=None, kind=None),
                                    Constant(value='product_product', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='add_table',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_template', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='add_where',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_product.template_id = product_template.id', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='alias', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='product_template', kind=None),
                                    Constant(value='categ_id', kind=None),
                                    Constant(value='product_category', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='categ_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='alias', ctx=Load()),
                                    Constant(value='product_template__categ_id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='alias', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='left_join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='product_product', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='res_user', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='user_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='alias', ctx=Load()),
                                    Constant(value='product_product__user_id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='from_clause', ctx=Store()),
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='where_params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='get_sql',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='from_clause', ctx=Load()),
                                    Constant(value='"product_product", "product_template" JOIN "product_category" AS "product_template__categ_id" ON ("product_template"."categ_id" = "product_template__categ_id"."id") LEFT JOIN "res_user" AS "product_product__user_id" ON ("product_product"."user_id" = "product_product__user_id"."id")', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='where_clause', ctx=Load()),
                                    Constant(value='product_product.template_id = product_template.id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_query_chained_explicit_joins',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Name(id='Query', ctx=Load()),
                                args=[
                                    Constant(value=None, kind=None),
                                    Constant(value='product_product', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='add_table',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_template', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='add_where',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_product.template_id = product_template.id', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='alias', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='product_template', kind=None),
                                    Constant(value='categ_id', kind=None),
                                    Constant(value='product_category', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='categ_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='alias', ctx=Load()),
                                    Constant(value='product_template__categ_id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='alias', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='left_join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='product_template__categ_id', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='res_user', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='user_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='alias', ctx=Load()),
                                    Constant(value='product_template__categ_id__user_id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='from_clause', ctx=Store()),
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='where_params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='get_sql',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='from_clause', ctx=Load()),
                                    Constant(value='"product_product", "product_template" JOIN "product_category" AS "product_template__categ_id" ON ("product_template"."categ_id" = "product_template__categ_id"."id") LEFT JOIN "res_user" AS "product_template__categ_id__user_id" ON ("product_template__categ_id"."user_id" = "product_template__categ_id__user_id"."id")', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='where_clause', ctx=Load()),
                                    Constant(value='product_product.template_id = product_template.id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mixed_query_chained_explicit_implicit_joins',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Name(id='Query', ctx=Load()),
                                args=[
                                    Constant(value=None, kind=None),
                                    Constant(value='product_product', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='add_table',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_template', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='add_where',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_product.template_id = product_template.id', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='alias', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='product_template', kind=None),
                                    Constant(value='categ_id', kind=None),
                                    Constant(value='product_category', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='categ_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='alias', ctx=Load()),
                                    Constant(value='product_template__categ_id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='alias', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='left_join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='product_template__categ_id', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='res_user', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='user_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='alias', ctx=Load()),
                                    Constant(value='product_template__categ_id__user_id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='add_table',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='account.account', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='add_where',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_category.expense_account_id = account_account.id', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='from_clause', ctx=Store()),
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='where_params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='get_sql',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='from_clause', ctx=Load()),
                                    Constant(value='"product_product", "product_template", "account.account" JOIN "product_category" AS "product_template__categ_id" ON ("product_template"."categ_id" = "product_template__categ_id"."id") LEFT JOIN "res_user" AS "product_template__categ_id__user_id" ON ("product_template__categ_id"."user_id" = "product_template__categ_id__user_id"."id")', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='where_clause', ctx=Load()),
                                    Constant(value='product_product.template_id = product_template.id AND product_category.expense_account_id = account_account.id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_raise_missing_lhs',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Name(id='Query', ctx=Load()),
                                args=[
                                    Constant(value=None, kind=None),
                                    Constant(value='product_product', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='query', ctx=Load()),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='product_template', kind=None),
                                            Constant(value='categ_id', kind=None),
                                            Constant(value='product_category', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='categ_id', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_long_aliases',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Name(id='Query', ctx=Load()),
                                args=[
                                    Constant(value=None, kind=None),
                                    Constant(value='product_product', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tmp', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='product_product', kind=None),
                                    Constant(value='product_tmpl_id', kind=None),
                                    Constant(value='product_template', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='product_tmpl_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tmp', ctx=Load()),
                                    Constant(value='product_product__product_tmpl_id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tmp_cat', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tmp', ctx=Load()),
                                    Constant(value='product_category_id', kind=None),
                                    Constant(value='product_category', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='product_category_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tmp_cat', ctx=Load()),
                                    Constant(value='product_product__product_tmpl_id__product_category_id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tmp_cat_cmp', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tmp_cat', ctx=Load()),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='res_company', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='company_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tmp_cat_cmp', ctx=Load()),
                                    Constant(value='product_product__product_tmpl_id__product_category_id__9f0ddff7', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tmp_cat_stm', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tmp_cat', ctx=Load()),
                                    Constant(value='salesteam_id', kind=None),
                                    Constant(value='res_company', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='salesteam_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tmp_cat_stm', ctx=Load()),
                                    Constant(value='product_product__product_tmpl_id__product_category_id__953a466f', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tmp_cat_cmp_par', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tmp_cat_cmp', ctx=Load()),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='res_partner', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tmp_cat_cmp_par', ctx=Load()),
                                    Constant(value='product_product__product_tmpl_id__product_category_id__56d55687', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tmp_cat_stm_par', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tmp_cat_stm', ctx=Load()),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='res_partner', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tmp_cat_stm_par', ctx=Load()),
                                    Constant(value='product_product__product_tmpl_id__product_category_id__00363fdd', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_table_expression',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Name(id='Query', ctx=Load()),
                                args=[
                                    Constant(value=None, kind=None),
                                    Constant(value='foo', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='from_clause', ctx=Store()),
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='where_params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='get_sql',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='from_clause', ctx=Load()),
                                    Constant(value='"foo"', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Name(id='Query', ctx=Load()),
                                args=[
                                    Constant(value=None, kind=None),
                                    Constant(value='bar', kind=None),
                                    Constant(value='SELECT id FROM foo', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='from_clause', ctx=Store()),
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='where_params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='get_sql',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='from_clause', ctx=Load()),
                                    Constant(value='(SELECT id FROM foo) AS "bar"', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Name(id='Query', ctx=Load()),
                                args=[
                                    Constant(value=None, kind=None),
                                    Constant(value='foo', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='add_table',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='bar', kind=None),
                                    Constant(value='SELECT id FROM foo', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='from_clause', ctx=Store()),
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='where_params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='get_sql',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='from_clause', ctx=Load()),
                                    Constant(value='"foo", (SELECT id FROM foo) AS "bar"', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Name(id='Query', ctx=Load()),
                                args=[
                                    Constant(value=None, kind=None),
                                    Constant(value='foo', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo', kind=None),
                                    Constant(value='bar_id', kind=None),
                                    Constant(value='SELECT id FROM foo', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='bar', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='from_clause', ctx=Store()),
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='where_params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='get_sql',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='from_clause', ctx=Load()),
                                    Constant(value='"foo" JOIN (SELECT id FROM foo) AS "foo__bar" ON ("foo"."bar_id" = "foo__bar"."id")', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
