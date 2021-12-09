Module(
    body=[
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='unslug', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteMembership',
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
                    name='members',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='membership_id', annotation=None, type_comment=None),
                            arg(arg='country_name', annotation=None, type_comment=None),
                            arg(arg='country_id', annotation=None, type_comment=None),
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
                            Constant(value=1, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Product', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.product', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Country', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.country', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='MembershipLine', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='membership.membership_line', kind=None),
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
                            targets=[Name(id='post_name', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='search', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='name', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_country', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='today', ctx=Store())],
                            value=Call(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_line_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='partner.website_published', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='paid', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_to', kind=None),
                                            Constant(value='>=', kind=None),
                                            Name(id='today', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_from', kind=None),
                                            Constant(value='<=', kind=None),
                                            Name(id='today', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='membership_id', ctx=Load()),
                                    Compare(
                                        left=Name(id='membership_id', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='free', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='membership_id', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='membership_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base_line_domain', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='membership_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='membership_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='post_name', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='base_line_domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='partner.name', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Name(id='post_name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='partner.website_description', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Name(id='post_name', ctx=Load()),
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
                        If(
                            test=Compare(
                                left=Name(id='membership_id', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='free', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='membership_lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='MembershipLine', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='base_line_domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='country_domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='member_lines', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='membership_lines', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='membership_id', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='country_domain', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Constant(value='|', kind=None),
                                                    Subscript(
                                                        value=Name(id='country_domain', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='membership_state', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='free', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='country_domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='membership_state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='free', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='post_name', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='country_domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Name(id='post_name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_description', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Name(id='post_name', ctx=Load()),
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
                                    BinOp(
                                        left=Name(id='country_domain', ctx=Load()),
                                        op=Add(),
                                        right=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='website_published', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Constant(value=True, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                            targets=[Name(id='countries_total', ctx=Store())],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='country_dict', ctx=Load()),
                                            slice=Constant(value='country_id_count', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='country_dict', ctx=Store()),
                                                iter=Name(id='countries', ctx=Load()),
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
                            targets=[Name(id='line_domain', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[Name(id='base_line_domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='country_id', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='line_domain', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='partner.country_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='country_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='current_country', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='Country', ctx=Load()),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='country_id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='read',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='name', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='any', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Compare(
                                                        left=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='x', ctx=Load()),
                                                                slice=Constant(value='country_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='country_id', ctx=Load())],
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
                                            keywords=[],
                                        ),
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
                                                                    Name(id='country_id', ctx=Load()),
                                                                    Subscript(
                                                                        value=Name(id='current_country', ctx=Load()),
                                                                        slice=Constant(value='name', kind=None),
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
                                        Assign(
                                            targets=[Name(id='countries', ctx=Store())],
                                            value=ListComp(
                                                elt=Name(id='d', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='d', ctx=Store()),
                                                        iter=Name(id='countries', ctx=Load()),
                                                        ifs=[
                                                            Subscript(
                                                                value=Name(id='d', ctx=Load()),
                                                                slice=Constant(value='country_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
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
                                                                value=Subscript(
                                                                    value=Name(id='d', ctx=Load()),
                                                                    slice=Constant(value='country_id', kind=None),
                                                                    ctx=Load(),
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
                                            Name(id='countries_total', ctx=Load()),
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
                            targets=[Name(id='memberships', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Product', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='membership', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
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
                                        value=Constant(value='website_sequence', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='line_domain', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='membership_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='memberships', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='limit', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_references_per_page',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='offset', ctx=Store())],
                            value=BinOp(
                                left=Name(id='limit', ctx=Load()),
                                op=Mult(),
                                right=BinOp(
                                    left=Name(id='page', ctx=Load()),
                                    op=Sub(),
                                    right=Constant(value=1, kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='count_members', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='membership_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='MembershipLine', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='membership_id', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='free', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='count_members', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='MembershipLine', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='line_domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='offset', ctx=Load()),
                                        ops=[LtE()],
                                        comparators=[Name(id='count_members', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='membership_lines', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='MembershipLine', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='line_domain', ctx=Load()),
                                                    Name(id='offset', ctx=Load()),
                                                    Name(id='limit', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='page_partner_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Attribute(
                                            value=Attribute(
                                                value=Name(id='m', ctx=Load()),
                                                attr='partner',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='m', ctx=Store()),
                                                iter=Name(id='membership_lines', ctx=Load()),
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
                            targets=[Name(id='google_map_partner_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='is_view_active',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website_membership.opt_index_google_map', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='google_map_partner_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='MembershipLine', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='line_domain', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='_get_published_companies',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=2000, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='search_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='membership_state', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='free', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='website_published', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='post_name', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='search_domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Name(id='post_name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_description', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Name(id='post_name', ctx=Load()),
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
                        If(
                            test=Name(id='country_id', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='search_domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='country_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='country_id', ctx=Load()),
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
                            targets=[Name(id='free_partners', ctx=Store())],
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
                                args=[Name(id='search_domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='memberships_data', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='membership_record', ctx=Store()),
                            iter=Name(id='memberships', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='memberships_data', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='membership_record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='membership_record', ctx=Load()),
                                                        attr='name',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='memberships_partner_ids', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='membership_lines', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='memberships_partner_ids', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='membership_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='partner',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='free_partners', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='memberships_data', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='free', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Free Members', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='membership_id', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Name(id='membership_id', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='free', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='count_members', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[
                                                    BinOp(
                                                        left=Name(id='offset', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='limit', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='free_start', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='max', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='offset', ctx=Load()),
                                                                op=Sub(),
                                                                right=Name(id='count_members', ctx=Load()),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='free_end', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='max', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Name(id='offset', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Name(id='limit', ctx=Load()),
                                                                ),
                                                                op=Sub(),
                                                                right=Name(id='count_members', ctx=Load()),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='memberships_partner_ids', ctx=Load()),
                                                            slice=Constant(value='free', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='free_partners', ctx=Load()),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Slice(
                                                            lower=Name(id='free_start', ctx=Load()),
                                                            upper=Name(id='free_end', ctx=Load()),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='page_partner_ids', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='memberships_partner_ids', ctx=Load()),
                                                                slice=Constant(value='free', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        AugAssign(
                                            target=Name(id='google_map_partner_ids', ctx=Store()),
                                            op=Add(),
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='free_partners', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=BinOp(
                                                        left=Constant(value=2000, kind=None),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='google_map_partner_ids', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='count_members', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='free_partners', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
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
                                                iter=Name(id='google_map_partner_ids', ctx=Load()),
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
                            targets=[Name(id='partners', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='p', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Name(id='p', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='p', ctx=Store()),
                                        iter=Call(
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
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Name(id='list', ctx=Load()),
                                                    args=[Name(id='page_partner_ids', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_url', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='/members%s%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        IfExp(
                                            test=Name(id='membership_id', ctx=Load()),
                                            body=BinOp(
                                                left=Constant(value='/association/%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='membership_id', ctx=Load()),
                                            ),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                        IfExp(
                                            test=Name(id='country_id', ctx=Load()),
                                            body=BinOp(
                                                left=Constant(value='/country/%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='country_id', ctx=Load()),
                                            ),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
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
                                        value=Name(id='base_url', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='total',
                                        value=Name(id='count_members', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='page',
                                        value=Name(id='page', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='step',
                                        value=Name(id='limit', ctx=Load()),
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
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='partners', kind=None),
                                    Constant(value='memberships_data', kind=None),
                                    Constant(value='memberships_partner_ids', kind=None),
                                    Constant(value='membership_id', kind=None),
                                    Constant(value='countries', kind=None),
                                    Constant(value='current_country', kind=None),
                                    Constant(value='current_country_id', kind=None),
                                    Constant(value='google_map_partner_ids', kind=None),
                                    Constant(value='pager', kind=None),
                                    Constant(value='post', kind=None),
                                    Constant(value='search', kind=None),
                                    Constant(value='search_count', kind=None),
                                    Constant(value='google_maps_api_key', kind=None),
                                ],
                                values=[
                                    Name(id='partners', ctx=Load()),
                                    Name(id='memberships_data', ctx=Load()),
                                    Name(id='memberships_partner_ids', ctx=Load()),
                                    Name(id='membership_id', ctx=Load()),
                                    Name(id='countries', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='current_country', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Subscript(
                                                                value=Name(id='current_country', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='current_country', ctx=Load()),
                                                                slice=Constant(value='name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='current_country', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='current_country', ctx=Load()),
                                                        slice=Constant(value='id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
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
                                    Name(id='count_members', ctx=Load()),
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
                                    Constant(value='website_membership.index', kind=None),
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
                                        Constant(value='/members', kind=None),
                                        Constant(value='/members/page/<int:page>', kind=None),
                                        Constant(value='/members/association/<membership_id>', kind=None),
                                        Constant(value='/members/association/<membership_id>/page/<int:page>', kind=None),
                                        Constant(value='/members/country/<int:country_id>', kind=None),
                                        Constant(value='/members/country/<country_name>-<int:country_id>', kind=None),
                                        Constant(value='/members/country/<int:country_id>/page/<int:page>', kind=None),
                                        Constant(value='/members/country/<country_name>-<int:country_id>/page/<int:page>', kind=None),
                                        Constant(value='/members/association/<membership_id>/country/<country_name>-<int:country_id>', kind=None),
                                        Constant(value='/members/association/<membership_id>/country/<int:country_id>', kind=None),
                                        Constant(value='/members/association/<membership_id>/country/<country_name>-<int:country_id>/page/<int:page>', kind=None),
                                        Constant(value='/members/association/<membership_id>/country/<int:country_id>/page/<int:page>', kind=None),
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
                                    value=Constant(value=True, kind=None),
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
                                                    Constant(value='website_membership.partner', kind=None),
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
                                    attr='members',
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
                                    elts=[Constant(value='/members/<partner_id>', kind=None)],
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
