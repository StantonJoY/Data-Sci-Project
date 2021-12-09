Module(
    body=[
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[
                alias(name='unslug', asname=None),
                alias(name='slug', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website.models.ir_http',
            names=[alias(name='sitemap_qs2dom', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteCustomer',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_references_per_page', ctx=Store())],
                    value=Constant(value=20, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='sitemap_industry',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='rule', annotation=None, type_comment=None),
                            arg(arg='qs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='qs', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='qs', ctx=Load()),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[In()],
                                        comparators=[Constant(value='/customers', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Dict(
                                            keys=[Constant(value='loc', kind=None)],
                                            values=[Constant(value='/customers', kind=None)],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='Industry', ctx=Store())],
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='res.partner.industry', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dom', ctx=Store())],
                            value=Call(
                                func=Name(id='sitemap_qs2dom', ctx=Load()),
                                args=[
                                    Name(id='qs', ctx=Load()),
                                    Constant(value='/customers/industry', kind=None),
                                    Attribute(
                                        value=Name(id='Industry', ctx=Load()),
                                        attr='_rec_name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='industry', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='Industry', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dom', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='loc', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/customers/industry/%s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='slug', ctx=Load()),
                                            args=[Name(id='industry', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='qs', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='qs', ctx=Load()),
                                                        attr='lower',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='loc', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Dict(
                                                    keys=[Constant(value='loc', kind=None)],
                                                    values=[Name(id='loc', ctx=Load())],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dom', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='website_published', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='assigned_partner_id', kind=None),
                                            Constant(value='!=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='!=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='dom', ctx=Store()),
                            op=Add(),
                            value=Call(
                                func=Name(id='sitemap_qs2dom', ctx=Load()),
                                args=[
                                    Name(id='qs', ctx=Load()),
                                    Constant(value='/customers/country', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='countries', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='dom', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='country_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='groupby',
                                        value=Constant(value='country_id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='country', ctx=Store()),
                            iter=Name(id='countries', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='loc', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/customers/country/%s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='slug', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='country', ctx=Load()),
                                                    slice=Constant(value='country_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='qs', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='qs', ctx=Load()),
                                                        attr='lower',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='loc', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Dict(
                                                    keys=[Constant(value='loc', kind=None)],
                                                    values=[Name(id='loc', ctx=Load())],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='customers',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='country', annotation=None, type_comment=None),
                            arg(arg='industry', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=0, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Tag', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner.tag', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Partner', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='search_value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='search', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='website_published', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='assigned_partner_id', kind=None),
                                            Constant(value='!=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='search_value', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Constant(value='|', kind=None),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Name(id='search_value', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_description', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Name(id='search_value', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='industry_id.name', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Name(id='search_value', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='tag_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='tag_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='tag_id', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Call(
                                                    func=Name(id='unslug', ctx=Load()),
                                                    args=[Name(id='tag_id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_tag_ids', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='tag_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='industries', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Partner', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='industry_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='groupby',
                                        value=Constant(value='industry_id', kind=None),
                                    ),
                                    keyword(
                                        arg='orderby',
                                        value=Constant(value='industry_id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partners_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Partner', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='industry', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='domain', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='industry_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='industry', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='industry', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            GeneratorExp(
                                                elt=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='x', ctx=Load()),
                                                        slice=Constant(value='industry_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Name(id='industries', ctx=Load()),
                                                        ifs=[
                                                            Subscript(
                                                                value=Name(id='x', ctx=Load()),
                                                                slice=Constant(value='industry_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='industry', ctx=Load()),
                                                    attr='exists',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='industries', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='industry_id_count', kind=None),
                                                                    Constant(value='industry_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=0, kind=None),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='industry', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='industry', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='industries', ctx=Load()),
                                    attr='sort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='d', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Subscript(
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='d', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='industry_id', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=0, kind=None),
                                                                Constant(value='', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='industries', ctx=Load()),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='industry_id_count', kind=None),
                                            Constant(value='industry_id', kind=None),
                                        ],
                                        values=[
                                            Name(id='partners_count', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='All Industries', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='countries', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Partner', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='country_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='groupby',
                                        value=Constant(value='country_id', kind=None),
                                    ),
                                    keyword(
                                        arg='orderby',
                                        value=Constant(value='country_id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Partner', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='country', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='country_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='country', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='country', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            GeneratorExp(
                                                elt=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='x', ctx=Load()),
                                                        slice=Constant(value='country_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Name(id='countries', ctx=Load()),
                                                        ifs=[
                                                            Subscript(
                                                                value=Name(id='x', ctx=Load()),
                                                                slice=Constant(value='country_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='country', ctx=Load()),
                                                    attr='exists',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='countries', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='country_id_count', kind=None),
                                                                    Constant(value='country_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=0, kind=None),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='country', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='country', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='countries', ctx=Load()),
                                                            attr='sort',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='key',
                                                                value=Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='d', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Subscript(
                                                                        value=BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Subscript(
                                                                                    value=Name(id='d', ctx=Load()),
                                                                                    slice=Constant(value='country_id', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Tuple(
                                                                                    elts=[
                                                                                        Constant(value=0, kind=None),
                                                                                        Constant(value='', kind=None),
                                                                                    ],
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        slice=Constant(value=1, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='countries', ctx=Load()),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id_count', kind=None),
                                            Constant(value='country_id', kind=None),
                                        ],
                                        values=[
                                            Name(id='country_count', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='All Countries', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='partner_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Partner', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Constant(value='/customers', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='industry', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='url', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='/industry/%s', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='industry', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='country', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='url', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='/country/%s', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='country', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='pager', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='pager',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url',
                                        value=Name(id='url', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='total',
                                        value=Name(id='partner_count', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='page',
                                        value=Name(id='page', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='step',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_references_per_page',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='scope',
                                        value=Constant(value=7, kind=None),
                                    ),
                                    keyword(
                                        arg='url_args',
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Partner', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Subscript(
                                            value=Name(id='pager', ctx=Load()),
                                            slice=Constant(value='offset', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_references_per_page',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='google_map_partner_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=',', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='it', ctx=Load())],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='it', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='partners', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='google_maps_api_key', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='website',
                                    ctx=Load(),
                                ),
                                attr='google_maps_api_key',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Tag', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_published', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='partner_ids', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='partners', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='classname, name ASC', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tag', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='tag_id', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Tag', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tag_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='countries', kind=None),
                                    Constant(value='current_country_id', kind=None),
                                    Constant(value='current_country', kind=None),
                                    Constant(value='industries', kind=None),
                                    Constant(value='current_industry_id', kind=None),
                                    Constant(value='current_industry', kind=None),
                                    Constant(value='partners', kind=None),
                                    Constant(value='google_map_partner_ids', kind=None),
                                    Constant(value='pager', kind=None),
                                    Constant(value='post', kind=None),
                                    Constant(value='search_path', kind=None),
                                    Constant(value='tag', kind=None),
                                    Constant(value='tags', kind=None),
                                    Constant(value='google_maps_api_key', kind=None),
                                ],
                                values=[
                                    Name(id='countries', ctx=Load()),
                                    IfExp(
                                        test=Name(id='country', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='country', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=0, kind=None),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='country', ctx=Load()),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Name(id='industries', ctx=Load()),
                                    IfExp(
                                        test=Name(id='industry', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='industry', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=0, kind=None),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='industry', ctx=Load()),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Name(id='partners', ctx=Load()),
                                    Name(id='google_map_partner_ids', ctx=Load()),
                                    Name(id='pager', ctx=Load()),
                                    Name(id='post', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='?%s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='werkzeug', ctx=Load()),
                                                    attr='urls',
                                                    ctx=Load(),
                                                ),
                                                attr='url_encode',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='post', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    Name(id='tag', ctx=Load()),
                                    Name(id='tags', ctx=Load()),
                                    Name(id='google_maps_api_key', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_customer.index', kind=None),
                                    Name(id='values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/customers', kind=None),
                                        Constant(value='/customers/page/<int:page>', kind=None),
                                        Constant(value='/customers/country/<model("res.country"):country>', kind=None),
                                        Constant(value='/customers/country/<model("res.country"):country>/page/<int:page>', kind=None),
                                        Constant(value='/customers/industry/<model("res.partner.industry"):industry>', kind=None),
                                        Constant(value='/customers/industry/<model("res.partner.industry"):industry>/page/<int:page>', kind=None),
                                        Constant(value='/customers/industry/<model("res.partner.industry"):industry>/country/<model("res.country"):country>', kind=None),
                                        Constant(value='/customers/industry/<model("res.partner.industry"):industry>/country/<model("res.country"):country>/page/<int:page>', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Name(id='sitemap_industry', ctx=Load()),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='partners_detail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='_', ctx=Store()),
                                        Name(id='partner_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='unslug', ctx=Load()),
                                args=[Name(id='partner_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='partner_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='partner', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='partner_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='exists',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='website_published',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='main_object', kind=None),
                                                    ctx=Store(),
                                                ),
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='partner', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='partner', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='render',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='website_customer.details', kind=None),
                                                    Name(id='values', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='customers',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[Constant(value='/customers/<partner_id>', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
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
