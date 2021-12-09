Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ClassDef(
            name='ResCompany',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.company', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='org_number', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_org_number', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_org_number',
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
                        For(
                            target=Name(id='company', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='company', ctx=Load()),
                                                        attr='account_fiscal_country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='SE', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='vat',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='org_number', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='sub',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='\\D', kind=None),
                                                        Constant(value='', kind=None),
                                                        Attribute(
                                                            value=Name(id='company', ctx=Load()),
                                                            attr='vat',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='org_number', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Subscript(
                                                        value=Name(id='org_number', ctx=Load()),
                                                        slice=Slice(
                                                            lower=None,
                                                            upper=Constant(value=6, kind=None),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value='-', kind=None),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='org_number', ctx=Load()),
                                                    slice=Slice(
                                                        lower=Constant(value=6, kind=None),
                                                        upper=None,
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='org_number',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='org_number', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='org_number',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='vat', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
