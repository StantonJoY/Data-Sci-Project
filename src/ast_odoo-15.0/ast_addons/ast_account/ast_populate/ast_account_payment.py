Module(
    body=[
        Expr(
            value=Constant(value='Classes defining the populate factory for Payments and related models.', kind=None),
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='populate', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='math', asname=None)],
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='lru_cache', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='AccountPayment',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Populate factory part for account.payment.', kind=None),
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='account.payment', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_sizes', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='small', kind=None),
                            Constant(value='medium', kind=None),
                            Constant(value='large', kind=None),
                        ],
                        values=[
                            Constant(value=100, kind=None),
                            Constant(value=5000, kind=None),
                            Constant(value=50000, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='res.company', kind=None),
                            Constant(value='res.partner', kind=None),
                            Constant(value='account.journal', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate_factories',
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
                            name='search_partner_ids',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='company_id', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value='Search all the partners that a company has access to.\n\n            This method is cached, only one search is done per company_id.\n            :param company_id (int): the company to search partners for.\n            :return (list<int>): the ids of partner the company has access to.\n            ', kind=None),
                                ),
                                Return(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.partner', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Constant(value='|', kind=None),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='company_id', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Name(id='company_id', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='company_id', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Constant(value=False, kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='id', kind=None),
                                                                Constant(value='in', kind=None),
                                                                Subscript(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='registry',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='populated_models',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='res.partner', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[
                                Call(
                                    func=Name(id='lru_cache', ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='search_journal_ids',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='company_id', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value='Search all the journal of a certain type for a company.\n\n            This method is cached, only one search is done per company_id.\n            :param company_id (int): the company to search journals for.\n            :return (list<int>): the ids of the bank and cash journals of a company\n            ', kind=None),
                                ),
                                Return(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='account.journal', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='company_id', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Name(id='company_id', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='type', kind=None),
                                                                Constant(value='in', kind=None),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='cash', kind=None),
                                                                        Constant(value='bank', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[
                                Call(
                                    func=Name(id='lru_cache', ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='search_payment_method_line_ids',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='payment_type', annotation=None, type_comment=None),
                                    arg(arg='journal', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value='Search all the payment methods of a certain type.\n\n            This method is cached, only one search is done per type.\n            :param payment_type (str): the type of payment method. Valid values are customer and supplier.\n            :param journal (int): the journal of the payment method.\n            :return list<int>: list of ids of payment methods of the selected type\n            ', kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='need_bank_account', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_method_codes_needing_bank_account',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='other_blacklist', ctx=Store())],
                                    value=List(
                                        elts=[Constant(value='sdd', kind=None)],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='account.payment.method.line', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='journal_id', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Name(id='journal', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='payment_method_id.payment_type', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Name(id='payment_type', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='code', kind=None),
                                                                Constant(value='not in', kind=None),
                                                                BinOp(
                                                                    left=Name(id='need_bank_account', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Name(id='other_blacklist', ctx=Load()),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[
                                Call(
                                    func=Name(id='lru_cache', ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_partner',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='random', annotation=None, type_comment=None),
                                    arg(arg='values', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value='Get a random partner depending on the company and the partner_type.\n\n            The first 3/5 of the available partners are used as customer\n            The last 3/5 of the available partners are used as suppliers\n            It means 1/5 is both customer/supplier\n            -> Same proportions as in account.move\n            :param random: seeded random number generator.\n            :param values (dict): the values already selected for the record.\n            :return (int): the id of the partner randomly selected.\n            ', kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='partner_type', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='partner_type', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='company_id', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='company_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='partner_ids', ctx=Store())],
                                    value=Call(
                                        func=Name(id='search_partner_ids', ctx=Load()),
                                        args=[Name(id='company_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='partner_type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='customer', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='random', ctx=Load()),
                                                    attr='choice',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='partner_ids', ctx=Load()),
                                                        slice=Slice(
                                                            lower=None,
                                                            upper=Call(
                                                                func=Attribute(
                                                                    value=Name(id='math', ctx=Load()),
                                                                    attr='ceil',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=BinOp(
                                                                            left=Call(
                                                                                func=Name(id='len', ctx=Load()),
                                                                                args=[Name(id='partner_ids', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            op=Div(),
                                                                            right=Constant(value=5, kind=None),
                                                                        ),
                                                                        op=Mult(),
                                                                        right=Constant(value=2, kind=None),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='random', ctx=Load()),
                                                    attr='choice',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='partner_ids', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Call(
                                                                func=Attribute(
                                                                    value=Name(id='math', ctx=Load()),
                                                                    attr='floor',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=BinOp(
                                                                            left=Call(
                                                                                func=Name(id='len', ctx=Load()),
                                                                                args=[Name(id='partner_ids', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            op=Div(),
                                                                            right=Constant(value=5, kind=None),
                                                                        ),
                                                                        op=Mult(),
                                                                        right=Constant(value=2, kind=None),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_journal',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='random', annotation=None, type_comment=None),
                                    arg(arg='values', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value='Get a random bank or cash journal depending on the company.\n\n            :param random: seeded random number generator.\n            :param values (dict): the values already selected for the record.\n            :return (int): the id of the journal randomly selected\n            ', kind=None),
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='choice',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='search_journal_ids', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='company_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
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
                            name='get_payment_method_line',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='random', annotation=None, type_comment=None),
                                    arg(arg='values', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value='Get the payment method depending on the payment type.\n\n            :param random: seeded random number generator.\n            :param values (dict): the values already selected for the record.\n            ', kind=None),
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='choice',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='search_payment_method_line_ids', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='payment_type', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='journal_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
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
                        Assign(
                            targets=[Name(id='company_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='chart_template_id', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='registry',
                                                                ctx=Load(),
                                                            ),
                                                            attr='populated_models',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.company', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='cartesian',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='company_ids', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='payment_type', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='cartesian',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='inbound', kind=None),
                                                            Constant(value='outbound', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='partner_type', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='cartesian',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='supplier', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='journal_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='get_journal', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='payment_method_line_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='get_payment_method_line', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='partner_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='get_partner', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='amount', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randfloat',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=1000, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randdatetime',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='relative_before',
                                                        value=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='years',
                                                                    value=UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=4, kind=None),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='size', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_populate',
                                    ctx=Load(),
                                ),
                                args=[Name(id='size', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Validating Payments', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='records', ctx=Load()),
                                                attr='move_id',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='r', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Lt()],
                                                    comparators=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='fields', ctx=Load()),
                                                                    attr='Date',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='today',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='records', ctx=Load()),
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
