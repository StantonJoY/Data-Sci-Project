Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='lxml', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.exceptions', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.wrappers', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='tools', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='slug', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website.models.ir_http',
            names=[alias(name='sitemap_qs2dom', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website_profile.controllers.main',
            names=[alias(name='WebsiteProfile', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.portal.controllers.portal',
            names=[alias(name='_build_url_w_params', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
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
            name='WebsiteForum',
            bases=[Name(id='WebsiteProfile', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_post_per_page', ctx=Store())],
                    value=Constant(value=10, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_user_per_page', ctx=Store())],
                    value=Constant(value=30, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_user_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='WebsiteForum', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='forum_welcome_message', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='cookies',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='forum_welcome_message', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='header', kind=None),
                                            Constant(value='searches', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='header', kind=None),
                                                    Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='searches', kind=None),
                                                    Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='forum', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='forum', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='forum', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='forum_id', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='forum', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='forum.forum', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='kwargs', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='forum_id', kind=None)],
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
                            ],
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='forum',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='website_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='forums', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='forum.forum', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='forums', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='/forum/%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='forums', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='code',
                                                value=Constant(value=302, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_forum.forum_all', kind=None),
                                    Dict(
                                        keys=[Constant(value='forums', kind=None)],
                                        values=[Name(id='forums', ctx=Load())],
                                    ),
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
                                    elts=[Constant(value='/forum', kind=None)],
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
                    name='forum_create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum_name', annotation=None, type_comment=None),
                            arg(arg='forum_mode', annotation=None, type_comment=None),
                            arg(arg='forum_privacy', annotation=None, type_comment=None),
                            arg(arg='forum_privacy_group', annotation=None, type_comment=None),
                            arg(arg='add_menu', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='New Forum', kind=None),
                            Constant(value='questions', kind=None),
                            Constant(value='public', kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='forum', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='mode', kind=None),
                                    Constant(value='privacy', kind=None),
                                    Constant(value='website_id', kind=None),
                                ],
                                values=[
                                    Name(id='forum_name', ctx=Load()),
                                    Name(id='forum_mode', ctx=Load()),
                                    Name(id='forum_privacy', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='website',
                                            ctx=Load(),
                                        ),
                                        attr='id',
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
                                        left=Name(id='forum_privacy', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='private', kind=None)],
                                    ),
                                    Name(id='forum_privacy_group', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='forum', ctx=Load()),
                                            slice=Constant(value='authorized_group_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='forum_privacy_group', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='forum_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='forum.forum', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='forum', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='add_menu', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='group', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='forum_privacy', ctx=Load()),
                                            ops=[Eq()],
                                            comparators=[Constant(value='private', kind=None)],
                                        ),
                                        body=List(
                                            elts=[
                                                Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[Name(id='forum_privacy_group', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        orelse=List(
                                            elts=[
                                                Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ref',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='base.group_portal', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ref',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='base.group_user', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='menu_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
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
                                                    Constant(value='parent_id', kind=None),
                                                    Constant(value='website_id', kind=None),
                                                    Constant(value='group_ids', kind=None),
                                                ],
                                                values=[
                                                    Name(id='forum_name', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='/forum/%s', kind=None),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Name(id='slug', ctx=Load()),
                                                            args=[Name(id='forum_id', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='website',
                                                                ctx=Load(),
                                                            ),
                                                            attr='menu_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='website',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=6, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Name(id='group', ctx=Load()),
                                                                ],
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
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='forum_id', ctx=Load()),
                                            attr='menu_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='menu_id', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='/forum/%s', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Name(id='slug', ctx=Load()),
                                    args=[Name(id='forum_id', ctx=Load())],
                                    keywords=[],
                                ),
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
                            args=[Constant(value='/forum/new', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='sitemap_forum',
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
                        Assign(
                            targets=[Name(id='Forum', ctx=Store())],
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='forum.forum', kind=None),
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
                                    Constant(value='/forum', kind=None),
                                    Attribute(
                                        value=Name(id='Forum', ctx=Load()),
                                        attr='_rec_name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='dom', ctx=Store()),
                            op=Add(),
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='website', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_current_website',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='website_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='f', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='Forum', ctx=Load()),
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
                                        left=Constant(value='/forum/%s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='slug', ctx=Load()),
                                            args=[Name(id='f', ctx=Load())],
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
                    name='questions',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='tag', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='filters', annotation=None, type_comment=None),
                            arg(arg='my', annotation=None, type_comment=None),
                            arg(arg='sorting', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=1, kind=None),
                            Constant(value='all', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='', kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Post', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='forum.post', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='sorting', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Post', ctx=Load()),
                                                    attr='_generate_order_by',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='sorting', ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='sorting', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='sorting', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sorting', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='forum', ctx=Load()),
                                        attr='default_order',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='options', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='displayDescription', kind=None),
                                    Constant(value='displayDetail', kind=None),
                                    Constant(value='displayExtraDetail', kind=None),
                                    Constant(value='displayExtraLink', kind=None),
                                    Constant(value='displayImage', kind=None),
                                    Constant(value='allowFuzzy', kind=None),
                                    Constant(value='forum', kind=None),
                                    Constant(value='tag', kind=None),
                                    Constant(value='filters', kind=None),
                                    Constant(value='my', kind=None),
                                ],
                                values=[
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='post', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='noFuzzy', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    IfExp(
                                        test=Name(id='forum', ctx=Load()),
                                        body=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='forum', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=None, kind=None),
                                    ),
                                    IfExp(
                                        test=Name(id='tag', ctx=Load()),
                                        body=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='tag', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=None, kind=None),
                                    ),
                                    Name(id='filters', ctx=Load()),
                                    Name(id='my', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='question_count', ctx=Store()),
                                        Name(id='details', ctx=Store()),
                                        Name(id='fuzzy_search_term', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='_search_with_fuzzy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='forum_posts_only', kind=None),
                                    Name(id='search', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=BinOp(
                                            left=Name(id='page', ctx=Load()),
                                            op=Mult(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_post_per_page',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Name(id='sorting', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='options',
                                        value=Name(id='options', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='question_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='details', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='results', kind=None),
                                    Name(id='Post', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='question_ids', ctx=Store())],
                            value=Subscript(
                                value=Name(id='question_ids', ctx=Load()),
                                slice=Slice(
                                    lower=BinOp(
                                        left=BinOp(
                                            left=Name(id='page', ctx=Load()),
                                            op=Sub(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                        op=Mult(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_post_per_page',
                                            ctx=Load(),
                                        ),
                                    ),
                                    upper=BinOp(
                                        left=Name(id='page', ctx=Load()),
                                        op=Mult(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_post_per_page',
                                            ctx=Load(),
                                        ),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='tag', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/forum/%s/tag/%s/questions', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='tag', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/forum/%s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='slug', ctx=Load()),
                                            args=[Name(id='forum', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='url_args', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='sorting', kind=None)],
                                values=[Name(id='sorting', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='search', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='url_args', ctx=Load()),
                                            slice=Constant(value='search', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='search', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='filters', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='url_args', ctx=Load()),
                                            slice=Constant(value='filters', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='filters', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='my', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='url_args', ctx=Load()),
                                            slice=Constant(value='my', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='my', ctx=Load()),
                                    type_comment=None,
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
                                        value=Name(id='question_count', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='page',
                                        value=Name(id='page', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='step',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_post_per_page',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='scope',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_post_per_page',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='url_args',
                                        value=Name(id='url_args', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='forum',
                                        value=Name(id='forum', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='searches',
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='header',
                                        value=Dict(
                                            keys=[Constant(value='ask_hide', kind=None)],
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='forum', ctx=Load()),
                                                        attr='active',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='main_object', kind=None),
                                            Constant(value='edit_in_backend', kind=None),
                                            Constant(value='question_ids', kind=None),
                                            Constant(value='question_count', kind=None),
                                            Constant(value='search_count', kind=None),
                                            Constant(value='pager', kind=None),
                                            Constant(value='tag', kind=None),
                                            Constant(value='filters', kind=None),
                                            Constant(value='my', kind=None),
                                            Constant(value='sorting', kind=None),
                                            Constant(value='search', kind=None),
                                            Constant(value='original_search', kind=None),
                                        ],
                                        values=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='tag', ctx=Load()),
                                                    Name(id='forum', ctx=Load()),
                                                ],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='tag', ctx=Load()),
                                            ),
                                            Name(id='question_ids', ctx=Load()),
                                            Name(id='question_count', ctx=Load()),
                                            Name(id='question_count', ctx=Load()),
                                            Name(id='pager', ctx=Load()),
                                            Name(id='tag', ctx=Load()),
                                            Name(id='filters', ctx=Load()),
                                            Name(id='my', ctx=Load()),
                                            Name(id='sorting', ctx=Load()),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='fuzzy_search_term', ctx=Load()),
                                                    Name(id='search', ctx=Load()),
                                                ],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='fuzzy_search_term', ctx=Load()),
                                                    Name(id='search', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_forum.forum_index', kind=None),
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
                                        Constant(value='/forum/<model("forum.forum"):forum>', kind=None),
                                        Constant(value='/forum/<model("forum.forum"):forum>/page/<int:page>', kind=None),
                                        Constant(value='/forum/<model("forum.forum"):forum>/tag/<model("forum.tag"):tag>/questions', kind=None),
                                        Constant(value='/forum/<model("forum.forum"):forum>/tag/<model("forum.tag"):tag>/questions/page/<int:page>', kind=None),
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
                                    value=Name(id='sitemap_forum', ctx=Load()),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='forum_faq',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='forum',
                                        value=Name(id='forum', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='searches',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='header',
                                        value=Dict(
                                            keys=[Constant(value='is_guidelines', kind=None)],
                                            values=[Constant(value=True, kind=None)],
                                        ),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
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
                                    Constant(value='website_forum.faq', kind=None),
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
                                    elts=[Constant(value='/forum/<model("forum.forum"):forum>/faq', kind=None)],
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
                    name='forum_faq_karma',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='forum',
                                        value=Name(id='forum', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='header',
                                        value=Dict(
                                            keys=[
                                                Constant(value='is_guidelines', kind=None),
                                                Constant(value='is_karma', kind=None),
                                            ],
                                            values=[
                                                Constant(value=True, kind=None),
                                                Constant(value=True, kind=None),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
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
                                    Constant(value='website_forum.faq_karma', kind=None),
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
                                    elts=[Constant(value='/forum/<model("forum.forum"):forum>/faq/karma', kind=None)],
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
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='tag_read',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='query', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value='', kind=None),
                            Constant(value=25, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='forum.tag', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='name', kind=None),
                                                        Constant(value='=ilike', kind=None),
                                                        BinOp(
                                                            left=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Name(id='query', ctx=Load()),
                                                                    Constant(value='', kind=None),
                                                                ],
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value='%', kind=None),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='id', kind=None),
                                                Constant(value='name', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[Name(id='limit', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
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
                            args=[Constant(value='/forum/get_tags', kind=None)],
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
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='tags',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='tag_char', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='first_char_tag', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='forum', ctx=Load()),
                                    attr='get_tags_first_char',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first_char_list', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Name(id='t', ctx=Load()),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='t', ctx=Store()),
                                        iter=Name(id='first_char_tag', ctx=Load()),
                                        ifs=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='t', ctx=Load()),
                                                    attr='isalnum',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
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
                                    value=Name(id='first_char_list', ctx=Load()),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='All', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='all', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='active_char_tag', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='tag_char', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tag_char', ctx=Load()),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Constant(value='all', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='forum_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='forum', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='posts_count', kind=None),
                                            Constant(value='>', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='order_by', ctx=Store())],
                            value=Constant(value='name', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='active_char_tag', ctx=Load()),
                                    Compare(
                                        left=Name(id='active_char_tag', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='all', kind=None)],
                                    ),
                                ],
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
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=ilike', kind=None),
                                                    BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='tools', ctx=Load()),
                                                                attr='escape_psql',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='active_char_tag', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='%', kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='order_by', ctx=Store())],
                                    value=Constant(value='posts_count DESC', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='forum.tag', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=None, kind=None),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Name(id='order_by', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='forum',
                                        value=Name(id='forum', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='searches',
                                        value=Dict(
                                            keys=[Constant(value='tags', kind=None)],
                                            values=[Constant(value=True, kind=None)],
                                        ),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='tags', kind=None),
                                            Constant(value='pager_tag_chars', kind=None),
                                            Constant(value='active_char_tag', kind=None),
                                        ],
                                        values=[
                                            Name(id='tags', ctx=Load()),
                                            Name(id='first_char_list', ctx=Load()),
                                            Name(id='active_char_tag', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_forum.tag', kind=None),
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
                                        Constant(value='/forum/<model("forum.forum"):forum>/tag', kind=None),
                                        Constant(value='/forum/<model("forum.forum"):forum>/tag/<string:tag_char>', kind=None),
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
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_url_title',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='req', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='url', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='req', ctx=Load()),
                                            attr='raise_for_status',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='arch', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='lxml', ctx=Load()),
                                                attr='html',
                                                ctx=Load(),
                                            ),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='req', ctx=Load()),
                                                attr='content',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='arch', ctx=Load()),
                                                attr='find',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='.//title', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/forum/get_url_title', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='old_question',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='_build_url_w_params', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='/forum/%s/%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='slug', ctx=Load()),
                                                            args=[Name(id='forum', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Name(id='slug', ctx=Load()),
                                                            args=[Name(id='question', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='params',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='code',
                                        value=Constant(value=301, kind=None),
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
                                    elts=[Constant(value='/forum/<model("forum.forum"):forum>/question/<model("forum.post", "[(\'forum_id\',\'=\',forum.id),(\'parent_id\',\'=\',False),(\'can_view\', \'=\', True)]"):question>', kind=None)],
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
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='question',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='forum', ctx=Load()),
                                    attr='active',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='website_forum.header', kind=None),
                                            Dict(
                                                keys=[Constant(value='forum', kind=None)],
                                                values=[Name(id='forum', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='question', ctx=Load()),
                                    attr='can_view',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='pending', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='karma',
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='forum', ctx=Load()),
                                                attr='karma_post',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='create_uid',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='user', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='question', ctx=Load()),
                                attr='parent_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='redirect_url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/forum/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='question', ctx=Load()),
                                                            attr='parent_id',
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
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='redirect_url', ctx=Load()),
                                            Constant(value=301, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
                            value=Constant(value='question', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='forum',
                                        value=Name(id='forum', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='searches',
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='main_object', kind=None),
                                            Constant(value='question', kind=None),
                                            Constant(value='can_bump', kind=None),
                                            Constant(value='header', kind=None),
                                            Constant(value='filters', kind=None),
                                            Constant(value='reversed', kind=None),
                                        ],
                                        values=[
                                            Name(id='question', ctx=Load()),
                                            Name(id='question', ctx=Load()),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='question', ctx=Load()),
                                                            attr='forum_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='allow_bump',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='question', ctx=Load()),
                                                            attr='child_count',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='datetime', ctx=Load()),
                                                                        attr='today',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                op=Sub(),
                                                                right=Attribute(
                                                                    value=Name(id='question', ctx=Load()),
                                                                    attr='write_date',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            attr='days',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=9, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='question_data', kind=None)],
                                                values=[Constant(value=True, kind=None)],
                                            ),
                                            Name(id='filters', ctx=Load()),
                                            Name(id='reversed', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='referrer',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='url_root',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='back_button_url', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='referrer',
                                        ctx=Load(),
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
                                            value=Name(id='question', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_set_viewed',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_forum.post_description_full', kind=None),
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
                                    elts=[Constant(value='/forum/<model("forum.forum"):forum>/<model("forum.post", "[(\'forum_id\',\'=\',forum.id),(\'parent_id\',\'=\',False),(\'can_view\', \'=\', True)]"):question>', kind=None)],
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
                    name='question_toggle_favorite',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='anonymous_user', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='favourite', ctx=Store())],
                            value=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='question', ctx=Load()),
                                    attr='user_favourite',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='favourite_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='favourite', ctx=Load()),
                                                            Constant(value=4, kind=None),
                                                        ],
                                                    ),
                                                    Constant(value=3, kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='uid',
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
                            test=Name(id='favourite', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='question', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='message_subscribe',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='favourite', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/toggle_favourite', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='question_ask_for_close',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='reasons', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='forum.post.reason', kind=None),
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
                                                    Constant(value='reason_type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='basic', kind=None),
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
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='question', kind=None),
                                            Constant(value='forum', kind=None),
                                            Constant(value='reasons', kind=None),
                                        ],
                                        values=[
                                            Name(id='question', ctx=Load()),
                                            Name(id='forum', ctx=Load()),
                                            Name(id='reasons', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_forum.close_post', kind=None),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/ask_for_close', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='question_edit_answer',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='question', ctx=Load()),
                                attr='child_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='create_uid',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='uid',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='answer', ctx=Store())],
                                            value=Name(id='record', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Break(),
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
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s/post/%s/edit', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='answer', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/edit_answer', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
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
                FunctionDef(
                    name='question_close',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='question', ctx=Load()),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='reason_id',
                                        value=Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='post', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='reason_id', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s/question/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='question', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/close', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='question_reopen',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwarg', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='question', ctx=Load()),
                                    attr='reopen',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='question', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/reopen', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='question_delete',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwarg', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='question', ctx=Load()),
                                    attr='active',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='question', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/delete', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='question_undelete',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwarg', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='question', ctx=Load()),
                                    attr='active',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='question', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/undelete', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='forum_post',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='email',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='single_email_re',
                                                    ctx=Load(),
                                                ),
                                                attr='match',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='email',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='/forum/%s/user/%s/edit?email_required=1', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='slug', ctx=Load()),
                                                            args=[Name(id='forum', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='session',
                                                                ctx=Load(),
                                                            ),
                                                            attr='uid',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='forum',
                                        value=Name(id='forum', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='searches',
                                        value=Dict(keys=[], values=[]),
                                    ),
                                    keyword(
                                        arg='header',
                                        value=Dict(
                                            keys=[Constant(value='ask_hide', kind=None)],
                                            values=[Constant(value=True, kind=None)],
                                        ),
                                    ),
                                    keyword(
                                        arg='new_question',
                                        value=Constant(value=True, kind=None),
                                    ),
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
                                    Constant(value='website_forum.new_question', kind=None),
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
                                    elts=[Constant(value='/forum/<model("forum.forum"):forum>/ask', kind=None)],
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
                                    value=Constant(value='user', kind=None),
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
                FunctionDef(
                    name='post_create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post_parent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='post', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='content', kind=None),
                                        Constant(value='', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='<p><br></p>', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='http_routing.http_error', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='status_code', kind=None),
                                                    Constant(value='status_message', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Bad Request', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='post_parent', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Reply should not be empty.', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Question should not be empty.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
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
                        Assign(
                            targets=[Name(id='post_tag_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='forum', ctx=Load()),
                                    attr='_tag_to_write_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='post_tags', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='forum_waiting_posts_count',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='/forum/%s/ask', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='new_question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='forum.post', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='forum_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='content', kind=None),
                                            Constant(value='parent_id', kind=None),
                                            Constant(value='tag_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='forum', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='post', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='post_name', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='post_parent', ctx=Load()),
                                                            BinOp(
                                                                left=Constant(value='Re: %s', kind=None),
                                                                op=Mod(),
                                                                right=BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='post_parent', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Constant(value='', kind=None),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='post', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='content', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='post_parent', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='post_parent', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Name(id='post_tag_ids', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Name(id='post_parent', ctx=Load()),
                                                                Call(
                                                                    func=Name(id='slug', ctx=Load()),
                                                                    args=[Name(id='post_parent', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                        Attribute(
                                                            value=Name(id='new_question', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                                        Constant(value='/forum/<model("forum.forum"):forum>/new', kind=None),
                                        Constant(value='/forum/<model("forum.forum"):forum>/<model("forum.post"):post_parent>/reply', kind=None),
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
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='post_comment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='question', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='parent_id',
                                    ctx=Load(),
                                ),
                                body=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='parent_id',
                                    ctx=Load(),
                                ),
                                orelse=Name(id='post', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='comment', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='post', ctx=Load()),
                                                attr='forum_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='forum', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='mail',
                                                ctx=Load(),
                                            ),
                                            attr='plaintext2html',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='kwargs', ctx=Load()),
                                                slice=Constant(value='comment', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='post', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='mail_create_nosubscribe',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Name(id='body', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='message_type',
                                                value=Constant(value='comment', kind=None),
                                            ),
                                            keyword(
                                                arg='subtype_xmlid',
                                                value=Constant(value='mail.mt_comment', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='question', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/comment', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='post_toggle_correct',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='parent_id',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=False, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='anonymous_user', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='post', ctx=Load()),
                                                attr='parent_id',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Name(id='post', ctx=Load()),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='is_correct',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='is_correct',
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='is_correct',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='post', ctx=Load()),
                                attr='is_correct',
                                ctx=Load(),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/toggle_correct', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
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
                FunctionDef(
                    name='post_delete',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='question', ctx=Store())],
                            value=Attribute(
                                value=Name(id='post', ctx=Load()),
                                attr='parent_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='question', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='/forum/%s/%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='slug', ctx=Load()),
                                                            args=[Name(id='forum', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Name(id='slug', ctx=Load()),
                                                            args=[Name(id='question', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='slug', ctx=Load()),
                                            args=[Name(id='forum', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/delete', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='post_edit',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='id',
                                            value=Attribute(
                                                value=Name(id='tag', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        keyword(
                                            arg='name',
                                            value=Attribute(
                                                value=Name(id='tag', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='tag', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='tag_ids',
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tags', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='forum',
                                        value=Name(id='forum', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='tags', kind=None),
                                            Constant(value='post', kind=None),
                                            Constant(value='is_edit', kind=None),
                                            Constant(value='is_answer', kind=None),
                                            Constant(value='searches', kind=None),
                                            Constant(value='content', kind=None),
                                        ],
                                        values=[
                                            Name(id='tags', ctx=Load()),
                                            Name(id='post', ctx=Load()),
                                            Constant(value=True, kind=None),
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='post', ctx=Load()),
                                                        attr='parent_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='kwargs', ctx=Load()),
                                            Attribute(
                                                value=Name(id='post', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_forum.edit_post', kind=None),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/edit', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
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
                FunctionDef(
                    name='post_save',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='content', kind=None)],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='content', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='post_name', kind=None),
                                ops=[In()],
                                comparators=[Name(id='kwargs', ctx=Load())],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='kwargs', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='post_name', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='strip',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='render',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='http_routing.http_error', kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='status_code', kind=None),
                                                            Constant(value='status_message', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Bad Request', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Title should not be empty.', kind=None)],
                                                                keywords=[],
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
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='post_name', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='vals', ctx=Load()),
                                    slice=Constant(value='tag_ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='forum', ctx=Load()),
                                    attr='_tag_to_write_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='post_tags', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='question', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='parent_id',
                                    ctx=Load(),
                                ),
                                body=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='parent_id',
                                    ctx=Load(),
                                ),
                                orelse=Name(id='post', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='question', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/save', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='post_upvote',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='anonymous_user', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='create_uid',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='own_post', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='upvote', ctx=Store())],
                            value=IfExp(
                                test=UnaryOp(
                                    op=Not(),
                                    operand=Compare(
                                        left=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='user_vote',
                                            ctx=Load(),
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                ),
                                body=Constant(value=True, kind=None),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='vote',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='upvote',
                                        value=Name(id='upvote', ctx=Load()),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/upvote', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
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
                FunctionDef(
                    name='post_downvote',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='anonymous_user', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='create_uid',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='own_post', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='upvote', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Attribute(
                                        value=Name(id='post', ctx=Load()),
                                        attr='user_vote',
                                        ctx=Load(),
                                    ),
                                    ops=[Lt()],
                                    comparators=[Constant(value=0, kind=None)],
                                ),
                                body=Constant(value=True, kind=None),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='vote',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='upvote',
                                        value=Name(id='upvote', ctx=Load()),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/downvote', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
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
                FunctionDef(
                    name='post_bump',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='post_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwarg', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='post', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='forum.post', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='post_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='post', ctx=Load()),
                                                attr='exists',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    Attribute(
                                        value=Name(id='post', ctx=Load()),
                                        attr='parent_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='bump',
                                    ctx=Load(),
                                ),
                                args=[],
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
                            args=[Constant(value='/forum/post/bump', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
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
                FunctionDef(
                    name='validation_queue',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='user', ctx=Load()),
                                    attr='karma',
                                    ctx=Load(),
                                ),
                                ops=[Lt()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='forum', ctx=Load()),
                                        attr='karma_moderate',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='Post', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='forum.post', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='forum_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='forum', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='pending', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='posts_to_validate_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Post', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='forum',
                                        value=Name(id='forum', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='posts_ids', kind=None),
                                            Constant(value='queue_type', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='posts_to_validate_ids', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='validation', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_forum.moderation_queue', kind=None),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/validation_queue', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
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
                FunctionDef(
                    name='flagged_queue',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='user', ctx=Load()),
                                    attr='karma',
                                    ctx=Load(),
                                ),
                                ops=[Lt()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='forum', ctx=Load()),
                                        attr='karma_moderate',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='Post', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='forum.post', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='forum_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='forum', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='flagged', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='spam_post', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='kwargs', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='spam_post', kind=None)],
                                                        keywords=[],
                                                    ),
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
                            targets=[Name(id='flagged_posts_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Post', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='write_date DESC', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='forum',
                                        value=Name(id='forum', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='posts_ids', kind=None),
                                            Constant(value='queue_type', kind=None),
                                            Constant(value='flagged_queue_active', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='flagged_posts_ids', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='flagged', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_forum.moderation_queue', kind=None),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/flagged_queue', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
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
                FunctionDef(
                    name='offensive_posts',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='user', ctx=Load()),
                                    attr='karma',
                                    ctx=Load(),
                                ),
                                ops=[Lt()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='forum', ctx=Load()),
                                        attr='karma_moderate',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='Post', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='forum.post', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='forum_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='forum', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='offensive', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='active', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='offensive_posts_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Post', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='write_date DESC', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='forum',
                                        value=Name(id='forum', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='posts_ids', kind=None),
                                            Constant(value='queue_type', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='offensive_posts_ids', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='offensive', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_forum.moderation_queue', kind=None),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/offensive_posts', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
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
                FunctionDef(
                    name='post_accept',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='/forum/%s/validation_queue', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Name(id='slug', ctx=Load()),
                                    args=[Name(id='forum', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='state',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='flagged', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/forum/%s/flagged_queue', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='slug', ctx=Load()),
                                            args=[Name(id='forum', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='offensive', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='url', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='/forum/%s/offensive_posts', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/validate', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
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
                FunctionDef(
                    name='post_refuse',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='refuse',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='question_ask_for_close',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='forum', ctx=Load()),
                                    Name(id='post', ctx=Load()),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/refuse', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
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
                FunctionDef(
                    name='post_flag',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='anonymous_user', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='post', ctx=Load()),
                                        attr='flag',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/flag', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
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
                FunctionDef(
                    name='post_ask_for_mark_as_offensive',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='offensive_reasons', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='forum.post.reason', kind=None),
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
                                                    Constant(value='reason_type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='offensive', kind=None),
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
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_user_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='forum',
                                        value=Name(id='forum', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='question', kind=None),
                                            Constant(value='forum', kind=None),
                                            Constant(value='reasons', kind=None),
                                            Constant(value='offensive', kind=None),
                                        ],
                                        values=[
                                            Name(id='post', ctx=Load()),
                                            Name(id='forum', ctx=Load()),
                                            Name(id='offensive_reasons', ctx=Load()),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_forum.close_post', kind=None),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/ask_for_mark_as_offensive', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='post_mark_as_offensive',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='mark_as_offensive',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='reason_id',
                                        value=Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='kwargs', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='reason_id', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='post', ctx=Load()),
                                attr='parent_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/forum/%s/%s/#answer-%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='post', ctx=Load()),
                                                        attr='parent_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='post', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/forum/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='post', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/mark_as_offensive', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='open_partner',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[Constant(value=0, kind=None)],
                    ),
                    body=[
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='partner_id', ctx=Load()),
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
                                            Name(id='partner', ctx=Load()),
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='user_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='/forum/%s/user/%d', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Name(id='slug', ctx=Load()),
                                                                    args=[Name(id='forum', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='partner', ctx=Load()),
                                                                            attr='user_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='slug', ctx=Load()),
                                            args=[Name(id='forum', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
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
                                    elts=[Constant(value='/forum/<model("forum.forum"):forum>/partner/<int:partner_id>', kind=None)],
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
                FunctionDef(
                    name='view_user_forum_profile',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='user_id', annotation=None, type_comment=None),
                            arg(arg='forum_origin', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=Constant(value='/profile/user/', kind=None),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='user_id', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value='?forum_id=', kind=None),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='forum', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            op=Add(),
                                            right=Constant(value='&forum_origin=', kind=None),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='forum_origin', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
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
                                    elts=[Constant(value='/forum/<model("forum.forum"):forum>/user/<int:user_id>', kind=None)],
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
                FunctionDef(
                    name='_prepare_user_profile_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='WebsiteForum', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_user_profile_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='post', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='no_forum', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='forum', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='forums', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='post', ctx=Load()),
                                                slice=Constant(value='forum', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='post', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='forum_id', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='forums', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='forum.forum', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='post', ctx=Load()),
                                                                        slice=Constant(value='forum_id', kind=None),
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
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='edit_button_url_param', kind=None),
                                                                    Constant(value='forum_filtered', kind=None),
                                                                ],
                                                                values=[
                                                                    BinOp(
                                                                        left=Constant(value='forum_id=%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Call(
                                                                            func=Name(id='str', ctx=Load()),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='post', ctx=Load()),
                                                                                    slice=Constant(value='forum_id', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='forums', ctx=Load()),
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
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='forums', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='forum.forum', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[List(elts=[], ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_prepare_user_values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='forum',
                                                        value=IfExp(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='forums', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                            body=Subscript(
                                                                value=Name(id='forums', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            orelse=Constant(value=True, kind=None),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='post', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='forums', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_prepare_open_forum_user',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='user', ctx=Load()),
                                                            Name(id='forums', ctx=Load()),
                                                        ],
                                                        keywords=[],
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
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_open_forum_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                            arg(arg='forums', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Post', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='forum.post', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Vote', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='forum.post.vote', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Activity', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mail.message', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Followers', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mail.followers', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Data', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.model.data', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_question_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Post', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='parent_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='forum_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='forums', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='create_uid', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='create_date desc', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='count_user_questions', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='user_question_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='min_karma_unlink', ctx=Store())],
                            value=Call(
                                func=Name(id='min', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='forums', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='karma_unlink_all', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='post_display_limit', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='karma',
                                    ctx=Load(),
                                ),
                                ops=[Lt()],
                                comparators=[Name(id='min_karma_unlink', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='post_display_limit', ctx=Store())],
                                    value=Constant(value=20, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='user_questions', ctx=Store())],
                            value=Subscript(
                                value=Name(id='user_question_ids', ctx=Load()),
                                slice=Slice(
                                    lower=None,
                                    upper=Name(id='post_display_limit', ctx=Load()),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_answer_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Post', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='parent_id', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='forum_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='forums', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='create_uid', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='create_date desc', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='count_user_answers', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='user_answer_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_answers', ctx=Store())],
                            value=Subscript(
                                value=Name(id='user_answer_ids', ctx=Load()),
                                slice=Slice(
                                    lower=None,
                                    upper=Name(id='post_display_limit', ctx=Load()),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='post_ids', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='follower', ctx=Load()),
                                    attr='res_id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='follower', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='Followers', ctx=Load()),
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
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='res_model', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Constant(value='forum.post', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='partner_id', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='user', ctx=Load()),
                                                                        attr='partner_id',
                                                                        ctx=Load(),
                                                                    ),
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
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='followed', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Post', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='post_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='forum_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='forums', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='parent_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
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
                        Assign(
                            targets=[Name(id='favourite', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Post', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='favourite_ids', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='forum_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='forums', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='parent_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
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
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Vote', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='forum_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='forums', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='recipient_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='vote', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='vote', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='up_votes', ctx=Store()),
                                        Name(id='down_votes', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rec', ctx=Store()),
                            iter=Name(id='data', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='rec', ctx=Load()),
                                            slice=Constant(value='vote', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='1', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='up_votes', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='rec', ctx=Load()),
                                                slice=Constant(value='vote_count', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='rec', ctx=Load()),
                                                    slice=Constant(value='vote', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='-1', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='down_votes', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='rec', ctx=Load()),
                                                        slice=Constant(value='vote_count', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
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
                        Assign(
                            targets=[Name(id='vote_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Vote', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='user_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='comment', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='Data', ctx=Load()),
                                        attr='_xmlid_lookup',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='mail.mt_comment', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=2, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='activities', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Activity', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=BinOp(
                                                            left=Name(id='user_question_ids', ctx=Load()),
                                                            op=Add(),
                                                            right=Name(id='user_answer_ids', ctx=Load()),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='model', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='forum.post', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='subtype_id', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Name(id='comment', ctx=Load()),
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
                                        value=Constant(value='date DESC', kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=100, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='posts', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='act', ctx=Store()),
                            iter=Name(id='activities', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='posts', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='act', ctx=Load()),
                                                attr='res_id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='posts_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Post', ctx=Load()),
                                    attr='search',
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
                                                        args=[Name(id='posts', ctx=Load())],
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
                        Assign(
                            targets=[Name(id='posts', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='x', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Tuple(
                                    elts=[
                                        BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='x', ctx=Load()),
                                                    attr='parent_id',
                                                    ctx=Load(),
                                                ),
                                                Name(id='x', ctx=Load()),
                                            ],
                                        ),
                                        BoolOp(
                                            op=Or(),
                                            values=[
                                                BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='parent_id',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='x', ctx=Load()),
                                                    ],
                                                ),
                                                Constant(value=False, kind=None),
                                            ],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Name(id='posts_ids', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='user', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='my_profile', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='users', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='uid', kind=None),
                                    Constant(value='user', kind=None),
                                    Constant(value='main_object', kind=None),
                                    Constant(value='searches', kind=None),
                                    Constant(value='questions', kind=None),
                                    Constant(value='count_questions', kind=None),
                                    Constant(value='answers', kind=None),
                                    Constant(value='count_answers', kind=None),
                                    Constant(value='followed', kind=None),
                                    Constant(value='favourite', kind=None),
                                    Constant(value='up_votes', kind=None),
                                    Constant(value='down_votes', kind=None),
                                    Constant(value='activities', kind=None),
                                    Constant(value='posts', kind=None),
                                    Constant(value='vote_post', kind=None),
                                    Constant(value='is_profile_page', kind=None),
                                    Constant(value='badge_category', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='user', ctx=Load()),
                                    Name(id='user', ctx=Load()),
                                    Name(id='kwargs', ctx=Load()),
                                    Name(id='user_questions', ctx=Load()),
                                    Name(id='count_user_questions', ctx=Load()),
                                    Name(id='user_answers', ctx=Load()),
                                    Name(id='count_user_answers', ctx=Load()),
                                    Name(id='followed', ctx=Load()),
                                    Name(id='favourite', ctx=Load()),
                                    Name(id='up_votes', ctx=Load()),
                                    Name(id='down_votes', ctx=Load()),
                                    Name(id='activities', ctx=Load()),
                                    Name(id='posts', ctx=Load()),
                                    Name(id='vote_ids', ctx=Load()),
                                    Constant(value=True, kind=None),
                                    Constant(value='forum', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='convert_comment_to_answer',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                            arg(arg='comment', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwarg', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='post', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='forum.post', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='convert_comment_to_answer',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='comment', ctx=Load()),
                                        attr='id',
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
                                operand=Name(id='post', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='/forum/%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='question', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='parent_id',
                                    ctx=Load(),
                                ),
                                body=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='parent_id',
                                    ctx=Load(),
                                ),
                                orelse=Name(id='post', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='question', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/comment/<model("mail.message"):comment>/convert_to_answer', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='convert_answer_to_comment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwarg', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='question', ctx=Store())],
                            value=Attribute(
                                value=Name(id='post', ctx=Load()),
                                attr='parent_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_msg', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='convert_answer_to_comment',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='new_msg', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='/forum/%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/forum/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='forum', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='slug', ctx=Load()),
                                                    args=[Name(id='question', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/convert_to_comment', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                FunctionDef(
                    name='delete_comment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='forum', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                            arg(arg='comment', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwarg', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='anonymous_user', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='post', ctx=Load()),
                                        attr='unlink_comment',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id='comment', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
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
                            args=[Constant(value='/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/comment/<model("mail.message"):comment>/delete', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
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
