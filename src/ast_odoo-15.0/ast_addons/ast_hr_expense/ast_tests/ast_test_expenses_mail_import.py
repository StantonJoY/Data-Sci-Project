Module(
    body=[
        ImportFrom(
            module='odoo.addons.hr_expense.tests.common',
            names=[alias(name='TestExpenseCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestExpensesMailImport',
            bases=[Name(id='TestExpenseCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='chart_template_ref', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='chart_template_ref',
                                        value=Name(id='chart_template_ref', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='product_a',
                                        ctx=Load(),
                                    ),
                                    attr='default_code',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='product_a', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='product_b',
                                        ctx=Load(),
                                    ),
                                    attr='default_code',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='product_b', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_import_expense_from_email',
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
                            targets=[Name(id='message_parsed', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='message_id', kind=None),
                                    Constant(value='subject', kind=None),
                                    Constant(value='email_from', kind=None),
                                    Constant(value='to', kind=None),
                                    Constant(value='body', kind=None),
                                    Constant(value='attachments', kind=None),
                                ],
                                values=[
                                    Constant(value='the-world-is-a-ghetto', kind=None),
                                    BinOp(
                                        left=Constant(value='%s %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_a',
                                                        ctx=Load(),
                                                    ),
                                                    attr='default_code',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_a',
                                                        ctx=Load(),
                                                    ),
                                                    attr='standard_price',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='expense_user_employee',
                                            ctx=Load(),
                                        ),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                    Constant(value='catchall@yourcompany.com', kind=None),
                                    Constant(value="Don't you know, that for me, and for you", kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expense', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.expense', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='message_new',
                                    ctx=Load(),
                                ),
                                args=[Name(id='message_parsed', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='expense', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='total_amount', kind=None),
                                                    Constant(value='employee_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_a',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=920.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='expense_employee',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
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
                    name='test_import_expense_from_email_no_product',
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
                            targets=[Name(id='message_parsed', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='message_id', kind=None),
                                    Constant(value='subject', kind=None),
                                    Constant(value='email_from', kind=None),
                                    Constant(value='to', kind=None),
                                    Constant(value='body', kind=None),
                                    Constant(value='attachments', kind=None),
                                ],
                                values=[
                                    Constant(value='the-world-is-a-ghetto', kind=None),
                                    Constant(value='no product code 800', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='expense_user_employee',
                                            ctx=Load(),
                                        ),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                    Constant(value='catchall@yourcompany.com', kind=None),
                                    Constant(value="Don't you know, that for me, and for you", kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expense', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.expense', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='message_new',
                                    ctx=Load(),
                                ),
                                args=[Name(id='message_parsed', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='expense', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='total_amount', kind=None),
                                                    Constant(value='employee_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=800.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='expense_employee',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
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
                    name='test_import_expense_from_mail_parsing_subjects',
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
                        FunctionDef(
                            name='assertParsedValues',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='subject', annotation=None, type_comment=None),
                                    arg(arg='currencies', annotation=None, type_comment=None),
                                    arg(arg='exp_description', annotation=None, type_comment=None),
                                    arg(arg='exp_amount', annotation=None, type_comment=None),
                                    arg(arg='exp_product', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='product', ctx=Store()),
                                                Name(id='amount', ctx=Store()),
                                                Name(id='currency_id', ctx=Store()),
                                                Name(id='description', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='hr.expense', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='expense_user_employee',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_parse_expense_subject',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='subject', ctx=Load()),
                                            Name(id='currencies', ctx=Load()),
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
                                            Name(id='product', ctx=Load()),
                                            Name(id='exp_product', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='amount', ctx=Load()),
                                            Name(id='exp_amount', ctx=Load()),
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
                                            Name(id='description', ctx=Load()),
                                            Name(id='exp_description', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assertParsedValues', ctx=Load()),
                                args=[
                                    Constant(value='product_a bar $1205.91 electro wizard', kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='currency', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='bar electro wizard', kind=None),
                                    Constant(value=1205.91, kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_a',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assertParsedValues', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='foo bar %s1406.91 royal giant', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='currency_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='currency', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='symbol',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='currency', kind=None),
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='foo bar %s royal giant', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='currency_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='currency', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='symbol',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value=1406.91, kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='expense_user_employee',
                                    ctx=Load(),
                                ),
                                attr='groups_id',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.group_multi_currency', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assertParsedValues', ctx=Load()),
                                args=[
                                    Constant(value='product_a foo bar $2205.92 elite barbarians', kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='currency', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='foo bar elite barbarians', kind=None),
                                    Constant(value=2205.92, kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_a',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assertParsedValues', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='product_a %s2510.90 chhota bheem', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='currency_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='currency', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='symbol',
                                            ctx=Load(),
                                        ),
                                    ),
                                    BinOp(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='currency_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='chhota bheem', kind=None),
                                    Constant(value=2510.9, kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_a',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assertParsedValues', ctx=Load()),
                                args=[
                                    Constant(value='foo bar 109.96 spear goblins', kind=None),
                                    BinOp(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='currency_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='foo bar spear goblins', kind=None),
                                    Constant(value=109.96, kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assertParsedValues', ctx=Load()),
                                args=[
                                    Constant(value='product_a foo bar 2910.94$ inferno dragon', kind=None),
                                    BinOp(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='currency_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='foo bar inferno dragon', kind=None),
                                    Constant(value=2910.94, kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_a',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assertParsedValues', ctx=Load()),
                                args=[
                                    Constant(value='foo bar mega knight', kind=None),
                                    BinOp(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='currency_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='foo bar mega knight', kind=None),
                                    Constant(value=0.0, kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assertParsedValues', ctx=Load()),
                                args=[
                                    Constant(value='foo bar 291,56$ mega knight', kind=None),
                                    BinOp(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='currency_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='foo bar mega knight', kind=None),
                                    Constant(value=291.56, kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assertParsedValues', ctx=Load()),
                                args=[
                                    Constant(value='foo bar 291$ mega knight', kind=None),
                                    BinOp(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='currency_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='foo bar mega knight', kind=None),
                                    Constant(value=291.0, kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assertParsedValues', ctx=Load()),
                                args=[
                                    Constant(value='product_a foo bar 291.5$ mega knight', kind=None),
                                    BinOp(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='currency_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='foo bar mega knight', kind=None),
                                    Constant(value=291.5, kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_a',
                                        ctx=Load(),
                                    ),
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
