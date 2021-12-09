Module(
    body=[
        ImportFrom(
            module='psycopg2',
            names=[alias(name='sql', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='slugify', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website.tools',
            names=[alias(name='text_from_html', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='escape_psql', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.safe_eval',
            names=[alias(name='safe_eval', asname=None)],
            level=0,
        ),
        ClassDef(
            name='Page',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='website.page', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherits', ctx=Store())],
                    value=Dict(
                        keys=[Constant(value='ir.ui.view', kind=None)],
                        values=[Constant(value='view_id', kind=None)],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='website.published.multi.mixin', kind=None),
                            Constant(value='website.searchable.mixin', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Page', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='website_id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Page URL', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='view_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.ui.view', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='View', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='website_indexed', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is Indexed', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_publish', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Publishing Date', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='menu_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='website.menu', kind=None),
                            Constant(value='page_id', kind=None),
                            Constant(value='Related Menus', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_homepage', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_homepage', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_homepage', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Homepage', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_visible', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_visible', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Is Visible', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cache_time', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=3600, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Time to cache the page. (0 = no cache)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cache_key_expr', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Expression (tuple) to evaluate the cached key. \nE.g.: "(request.params.get("currency"), )"', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='header_overlay', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='header_color', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='header_visible', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='footer_visible', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='website_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='view_id.website_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='arch', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='view_id.arch', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='depends_context',
                                value=Tuple(
                                    elts=[Constant(value='website_id', kind=None)],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_homepage',
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
                            target=Name(id='page', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='page', ctx=Load()),
                                            attr='is_homepage',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        left=Name(id='page', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='website', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='get_current_website',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='homepage_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
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
                    name='_set_homepage',
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
                            target=Name(id='page', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='website', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_current_website',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='page', ctx=Load()),
                                        attr='is_homepage',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='homepage_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Name(id='page', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='website', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='homepage_id', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='page', ctx=Load()),
                                                                        attr='id',
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
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='homepage_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='page', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='website', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='homepage_id', kind=None)],
                                                                values=[Constant(value=None, kind=None)],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
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
                    name='_compute_visible',
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
                            target=Name(id='page', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='page', ctx=Load()),
                                            attr='is_visible',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='page', ctx=Load()),
                                                attr='website_published',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='page', ctx=Load()),
                                                            attr='date_publish',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='page', ctx=Load()),
                                                            attr='date_publish',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Lt()],
                                                        comparators=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Datetime',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='now',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
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
                    name='_get_most_specific_pages',
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
                        Expr(
                            value=Constant(value=' Returns the most specific pages in self. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='previous_page', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='page', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='p', ctx=Load()),
                                                            attr='website_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='previous_page', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='page', ctx=Load()),
                                                    attr='url',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='previous_page', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='page', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='previous_page', ctx=Store())],
                                    value=Name(id='page', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='page', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='page', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[Name(id='ids', ctx=Load())],
                                        ),
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
                    name='get_page_properties',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='read',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Constant(value='id', kind=None),
                                                Constant(value='view_id', kind=None),
                                                Constant(value='name', kind=None),
                                                Constant(value='url', kind=None),
                                                Constant(value='website_published', kind=None),
                                                Constant(value='website_indexed', kind=None),
                                                Constant(value='date_publish', kind=None),
                                                Constant(value='menu_ids', kind=None),
                                                Constant(value='is_homepage', kind=None),
                                                Constant(value='website_id', kind=None),
                                                Constant(value='visibility', kind=None),
                                                Constant(value='groups_id', kind=None),
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
                                operand=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='groups_id', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='group_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
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
                                                    args=[Constant(value='base.group_user', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='name_get',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='groups_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='group_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
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
                                                                    slice=Constant(value='res.groups', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='browse',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    slice=Constant(value='groups_id', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='name_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Delete(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='groups_id', kind=None),
                                    ctx=Del(),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='visibility_password', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='visibility', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='password', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='visibility_password_display',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save_page_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='website_id', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='website_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='page', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='original_url', ctx=Store())],
                            value=Attribute(
                                value=Name(id='page', ctx=Load()),
                                attr='url',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Subscript(
                                value=Name(id='data', ctx=Load()),
                                slice=Constant(value='url', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='url', ctx=Load()),
                                        attr='startswith',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='/', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/', kind=None),
                                        op=Add(),
                                        right=Name(id='url', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='page', ctx=Load()),
                                    attr='url',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Name(id='url', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/', kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='slugify', ctx=Load()),
                                            args=[Name(id='url', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='max_length',
                                                    value=Constant(value=1024, kind=None),
                                                ),
                                                keyword(
                                                    arg='path',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_unique_path',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='url', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='page', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='page_key', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_unique_key',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='slugify', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='page_key', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='page', ctx=Load()),
                                        attr='key',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='menu', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.menu', kind=None),
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
                                                    Constant(value='page_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='data', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='is_menu', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                If(
                                    test=Name(id='menu', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='menu', ctx=Load()),
                                                    attr='unlink',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='menu', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='menu', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='url', kind=None)],
                                                        values=[Name(id='url', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website.menu', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='url', kind=None),
                                                            Constant(value='page_id', kind=None),
                                                            Constant(value='parent_id', kind=None),
                                                            Constant(value='website_id', kind=None),
                                                        ],
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='data', ctx=Load()),
                                                                slice=Constant(value='name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='url', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='data', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='website', ctx=Load()),
                                                                    attr='menu_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='website', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='w_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='key', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='url', kind=None),
                                    Constant(value='is_published', kind=None),
                                    Constant(value='website_indexed', kind=None),
                                    Constant(value='date_publish', kind=None),
                                    Constant(value='is_homepage', kind=None),
                                    Constant(value='visibility', kind=None),
                                ],
                                values=[
                                    Name(id='page_key', ctx=Load()),
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='url', ctx=Load()),
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='website_published', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='website_indexed', kind=None),
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Constant(value='date_publish', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                    ),
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='is_homepage', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='visibility', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='page', ctx=Load()),
                                            attr='visibility',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='restricted_group', kind=None)],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='visibility', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='restricted_group', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='w_vals', ctx=Load()),
                                            slice=Constant(value='groups_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Constant(value='group_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='data', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='w_vals', ctx=Load()),
                                                    slice=Constant(value='groups_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='group_id', kind=None),
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
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='visibility_pwd', kind=None),
                                ops=[In()],
                                comparators=[Name(id='data', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='w_vals', ctx=Load()),
                                            slice=Constant(value='visibility_password_display', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Constant(value='visibility_pwd', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='page', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='no_cow',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='w_vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='data', ctx=Load()),
                                slice=Constant(value='create_redirect', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.rewrite', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='redirect_type', kind=None),
                                                    Constant(value='url_from', kind=None),
                                                    Constant(value='url_to', kind=None),
                                                    Constant(value='website_id', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='redirect_type', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='original_url', ctx=Load()),
                                                    Name(id='url', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='website', ctx=Load()),
                                                        attr='id',
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
                        Return(
                            value=Name(id='url', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='copy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Name(id='default', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='default', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='view_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='view', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.ui.view', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='view_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='new_view', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='view', ctx=Load()),
                                                    attr='copy',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='website_id', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='default', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='website_id', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='default', ctx=Load()),
                                                    slice=Constant(value='view_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='new_view', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='default', ctx=Load()),
                                            slice=Constant(value='url', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='default', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='url', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_unique_path',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Page', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Name(id='default', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='returns',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='self', kind=None),
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='value', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clone_page',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page_id', annotation=None, type_comment=None),
                            arg(arg='page_name', annotation=None, type_comment=None),
                            arg(arg='clone_menu', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Clone a page, given its identifier\n            :param page_id : website.page identifier\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='page', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='page_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='copy_param', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='page_name', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='page', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_current_website',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='page_name', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='page_url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/', kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='slugify', ctx=Load()),
                                            args=[Name(id='page_name', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='max_length',
                                                    value=Constant(value=1024, kind=None),
                                                ),
                                                keyword(
                                                    arg='path',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='copy_param', ctx=Load()),
                                            slice=Constant(value='url', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_unique_path',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='page_url', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='new_page', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='page', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[Name(id='copy_param', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='clone_menu', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='new_page', ctx=Load()),
                                            attr='website_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='page', ctx=Load()),
                                                attr='website_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='menu', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.menu', kind=None),
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
                                                            Constant(value='page_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='page_id', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='menu', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='menu', ctx=Load()),
                                                    attr='copy',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='url', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='page_id', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='new_page', ctx=Load()),
                                                                attr='url',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='new_page', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='new_page', ctx=Load()),
                                                                attr='id',
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
                        Return(
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='new_page', ctx=Load()),
                                    attr='url',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Constant(value='?enable_editor=1', kind=None),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                            target=Name(id='page', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='pages_linked_to_iruiview', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='view_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='page', ctx=Load()),
                                                                    attr='view_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Attribute(
                                                                value=Name(id='page', ctx=Load()),
                                                                attr='id',
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
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='pages_linked_to_iruiview', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='page', ctx=Load()),
                                                        attr='view_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='inherit_children_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='page', ctx=Load()),
                                                        attr='view_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='unlink',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Page', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
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
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='url', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='url', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='/', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='url', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='/', kind=None),
                                        op=Add(),
                                        right=Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='url', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Page', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_website_meta',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='view_id',
                                        ctx=Load(),
                                    ),
                                    attr='get_website_meta',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_cached_blacklist',
                    args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value='data-snippet="s_website_form"', kind=None),
                                    Constant(value='data-no-page-cache=', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='staticmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_can_be_cached',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='response', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" return False if at least one blacklisted's word is present in content ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='blacklist', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_cached_blacklist',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='any', ctx=Load()),
                                    args=[
                                        GeneratorExp(
                                            elt=Compare(
                                                left=Name(id='black', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='response', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='black', ctx=Store()),
                                                    iter=Name(id='blacklist', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_cache_key',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='req', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cache_key', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='req', ctx=Load()),
                                            attr='website',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='req', ctx=Load()),
                                        attr='lang',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='req', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='cache_key_expr',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='cache_key', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Name(id='safe_eval', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cache_key_expr',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='request', kind=None)],
                                                values=[Name(id='req', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='cache_key', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_cache_response',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cache_key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the cached response corresponding to ``self`` and ``cache_key``.\n        Raise a KeyError if the item is not in cache.\n        ', kind=None),
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pool',
                                        ctx=Load(),
                                    ),
                                    attr='_Registry__cache',
                                    ctx=Load(),
                                ),
                                slice=Tuple(
                                    elts=[
                                        Constant(value='website.page', kind=None),
                                        Name(id='_cached_response', ctx=Load()),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Name(id='cache_key', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_cache_response',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cache_key', annotation=None, type_comment=None),
                            arg(arg='response', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Put in cache the given response. ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='pool',
                                            ctx=Load(),
                                        ),
                                        attr='_Registry__cache',
                                        ctx=Load(),
                                    ),
                                    slice=Tuple(
                                        elts=[
                                            Constant(value='website.page', kind=None),
                                            Name(id='_cached_response', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='cache_key', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='response', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_get_detail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='website', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='with_description', ctx=Store())],
                            value=Subscript(
                                value=Name(id='options', ctx=Load()),
                                slice=Constant(value='displayDescription', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='requires_sudo', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='website', ctx=Load()),
                                            attr='website_domain',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='has_group',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='website.group_website_designer', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='domain', ctx=Load()),
                                            attr='append',
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
                        Assign(
                            targets=[Name(id='search_fields', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='name', kind=None),
                                    Constant(value='url', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fetch_fields', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='id', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='url', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapping', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='website_url', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='match', kind=None),
                                        ],
                                        values=[
                                            Constant(value='name', kind=None),
                                            Constant(value='text', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='url', kind=None),
                                            Constant(value='text', kind=None),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='with_description', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='search_fields', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='arch_db', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fetch_fields', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='arch', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='mapping', ctx=Load()),
                                            slice=Constant(value='description', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='html', kind=None),
                                            Constant(value='match', kind=None),
                                        ],
                                        values=[
                                            Constant(value='arch', kind=None),
                                            Constant(value='text', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='model', kind=None),
                                    Constant(value='base_domain', kind=None),
                                    Constant(value='requires_sudo', kind=None),
                                    Constant(value='search_fields', kind=None),
                                    Constant(value='fetch_fields', kind=None),
                                    Constant(value='mapping', kind=None),
                                    Constant(value='icon', kind=None),
                                ],
                                values=[
                                    Constant(value='website.page', kind=None),
                                    Name(id='domain', ctx=Load()),
                                    Name(id='requires_sudo', ctx=Load()),
                                    Name(id='search_fields', ctx=Load()),
                                    Name(id='fetch_fields', ctx=Load()),
                                    Name(id='mapping', ctx=Load()),
                                    Constant(value='fa-file-o', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_fetch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='search_detail', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='with_description', ctx=Store())],
                            value=Compare(
                                left=Constant(value='description', kind=None),
                                ops=[In()],
                                comparators=[
                                    Subscript(
                                        value=Name(id='search_detail', ctx=Load()),
                                        slice=Constant(value='mapping', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='results', ctx=Store()),
                                        Name(id='count', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_search_fetch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='search_detail', ctx=Load()),
                                    Name(id='search', ctx=Load()),
                                    Name(id='limit', ctx=Load()),
                                    Name(id='order', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='with_description', ctx=Load()),
                                    Name(id='search', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='SQL',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value="\n                SELECT {table}.{id}\n                FROM {table}\n                LEFT JOIN ir_ui_view v ON {table}.{view_id} = v.{id}\n                LEFT JOIN ir_translation t ON v.{id} = t.{res_id}\n                WHERE t.lang = {lang}\n                AND t.name = ANY({names})\n                AND t.type = 'model_terms'\n                AND t.value ilike {search}\n                LIMIT {limit}\n            ", kind=None)],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='table',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='sql', ctx=Load()),
                                                        attr='Identifier',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_table',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='id',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='sql', ctx=Load()),
                                                        attr='Identifier',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='view_id',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='sql', ctx=Load()),
                                                        attr='Identifier',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='view_id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='res_id',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='sql', ctx=Load()),
                                                        attr='Identifier',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='res_id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='lang',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='sql', ctx=Load()),
                                                        attr='Placeholder',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='lang', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='names',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='sql', ctx=Load()),
                                                        attr='Placeholder',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='names', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='search',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='sql', ctx=Load()),
                                                        attr='Placeholder',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='search', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='limit',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='sql', ctx=Load()),
                                                        attr='Placeholder',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='limit', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='query', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='names', kind=None),
                                                    Constant(value='search', kind=None),
                                                    Constant(value='limit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='lang',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='ir.ui.view,arch_db', kind=None),
                                                            Constant(value='ir.ui.view,name', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='%%%s%%', kind=None),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Name(id='escape_psql', ctx=Load()),
                                                            args=[Name(id='search', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Name(id='limit', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='ids', ctx=Store())],
                                    value=SetComp(
                                        elt=Subscript(
                                            value=Name(id='row', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='row', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='cr',
                                                            ctx=Load(),
                                                        ),
                                                        attr='fetchall',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ids', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='results', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='domains', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='search_detail', ctx=Load()),
                                                slice=Constant(value='base_domain', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='copy',
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
                                            value=Name(id='domains', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Call(
                                                                func=Name(id='list', ctx=Load()),
                                                                args=[Name(id='ids', ctx=Load())],
                                                                keywords=[],
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
                                ),
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domains', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=IfExp(
                                        test=Call(
                                            func=Attribute(
                                                value=Name(id='search_detail', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='requires_sudo', kind=None)],
                                            keywords=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        orelse=Name(id='self', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='results', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Name(id='limit', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='order',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='search_detail', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='order', kind=None),
                                                        Name(id='order', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='count', ctx=Store())],
                                    value=Call(
                                        func=Name(id='max', ctx=Load()),
                                        args=[
                                            Name(id='count', ctx=Load()),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='results', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        FunctionDef(
                            name='filter_page',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='search', annotation=None, type_comment=None),
                                    arg(arg='page', annotation=None, type_comment=None),
                                    arg(arg='all_pages', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='text', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s %s %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='page', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='page', ctx=Load()),
                                                    attr='url',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Name(id='text_from_html', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='page', ctx=Load()),
                                                            attr='arch',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pattern', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='|', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='escape',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='search_term', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='search_term', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='search', ctx=Load()),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
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
                                Return(
                                    value=IfExp(
                                        test=Name(id='pattern', ctx=Load()),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='re', ctx=Load()),
                                                attr='findall',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                BinOp(
                                                    left=Constant(value='(%s)', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='pattern', ctx=Load()),
                                                ),
                                                Name(id='text', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='flags',
                                                    value=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='I',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='url', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='order', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='results', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='results', ctx=Load()),
                                            attr='_get_most_specific_pages',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='search', ctx=Load()),
                                    Name(id='with_description', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='results', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='results', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='result', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Call(
                                                    func=Name(id='filter_page', ctx=Load()),
                                                    args=[
                                                        Name(id='search', ctx=Load()),
                                                        Name(id='result', ctx=Load()),
                                                        Name(id='results', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='results', ctx=Load()),
                                    Name(id='count', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='_cached_response',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[Pass()],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
