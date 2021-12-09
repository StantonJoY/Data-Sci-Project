Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.im_livechat.controllers.main',
            names=[alias(name='LivechatController', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteLivechat',
            bases=[Name(id='LivechatController', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='channel_list',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='channels', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='im_livechat.channel', kind=None),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='channels', kind=None)],
                                values=[Name(id='channels', ctx=Load())],
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
                                    Constant(value='website_livechat.channel_list_page', kind=None),
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
                            args=[Constant(value='/livechat', kind=None)],
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
                    name='channel_rating',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='channel', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='mail.channel', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='res_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='channel', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='channel_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='consumed', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='rating', kind=None),
                                            Constant(value='>=', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ratings', ctx=Store())],
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
                                                slice=Constant(value='rating.rating', kind=None),
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
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='create_date desc', kind=None),
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
                            targets=[Name(id='repartition', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_ids',
                                        ctx=Load(),
                                    ),
                                    attr='rating_get_grades',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=Name(id='domain', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='percentage', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='great', kind=None),
                                            Constant(value='okay', kind=None),
                                            Constant(value='bad', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='grade', ctx=Store()),
                            iter=Name(id='repartition', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='percentage', ctx=Load()),
                                            slice=Name(id='grade', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='repartition', ctx=Load()),
                                                        attr='values',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        body=Call(
                                            func=Name(id='round', ctx=Load()),
                                            args=[
                                                BinOp(
                                                    left=BinOp(
                                                        left=Subscript(
                                                            value=Name(id='repartition', ctx=Load()),
                                                            slice=Name(id='grade', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        op=Mult(),
                                                        right=Constant(value=100.0, kind=None),
                                                    ),
                                                    op=Div(),
                                                    right=Call(
                                                        func=Name(id='sum', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='repartition', ctx=Load()),
                                                                    attr='values',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Constant(value=1, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=0, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ratings_per_partner', ctx=Store())],
                            value=DictComp(
                                key=Name(id='partner_id', ctx=Load()),
                                value=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='great',
                                            value=Constant(value=0, kind=None),
                                        ),
                                        keyword(
                                            arg='okay',
                                            value=Constant(value=0, kind=None),
                                        ),
                                        keyword(
                                            arg='bad',
                                            value=Constant(value=0, kind=None),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='partner_id', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='ratings', ctx=Load()),
                                                attr='mapped',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='rated_partner_id.id', kind=None)],
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
                            targets=[Name(id='total_ratings_per_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='ratings', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='rated_partner_id.id', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rating_texts', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value=10, kind=None),
                                    Constant(value=5, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                values=[
                                    Constant(value='great', kind=None),
                                    Constant(value='great', kind=None),
                                    Constant(value='okay', kind=None),
                                    Constant(value='bad', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rating', ctx=Store()),
                            iter=Name(id='ratings', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='partner_id', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='rating', ctx=Load()),
                                            attr='rated_partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Subscript(
                                        value=Subscript(
                                            value=Name(id='ratings_per_partner', ctx=Load()),
                                            slice=Name(id='partner_id', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        slice=Subscript(
                                            value=Name(id='rating_texts', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='rating', ctx=Load()),
                                                attr='rating',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='total_ratings_per_partner', ctx=Load()),
                                        slice=Name(id='partner_id', ctx=Load()),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='partner_id', ctx=Store()),
                                    Name(id='rating', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='ratings_per_partner', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='k', ctx=Store()),
                                            Name(id='v', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='ratings_per_partner', ctx=Load()),
                                                slice=Name(id='partner_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='ratings_per_partner', ctx=Load()),
                                                        slice=Name(id='partner_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='k', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='round', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Constant(value=100, kind=None),
                                                            op=Mult(),
                                                            right=Name(id='v', ctx=Load()),
                                                        ),
                                                        op=Div(),
                                                        right=Subscript(
                                                            value=Name(id='total_ratings_per_partner', ctx=Load()),
                                                            slice=Name(id='partner_id', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='main_object', kind=None),
                                    Constant(value='channel', kind=None),
                                    Constant(value='ratings', kind=None),
                                    Constant(value='team', kind=None),
                                    Constant(value='percentage', kind=None),
                                    Constant(value='ratings_per_user', kind=None),
                                ],
                                values=[
                                    Name(id='channel', ctx=Load()),
                                    Name(id='channel', ctx=Load()),
                                    Name(id='ratings', ctx=Load()),
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='user_ids',
                                        ctx=Load(),
                                    ),
                                    Name(id='percentage', ctx=Load()),
                                    Name(id='ratings_per_partner', ctx=Load()),
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
                                    Constant(value='website_livechat.channel_page', kind=None),
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
                            args=[Constant(value='/livechat/channel/<model("im_livechat.channel"):channel>', kind=None)],
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
                    name='get_session',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='channel_id', annotation=None, type_comment=None),
                            arg(arg='anonymous_name', annotation=None, type_comment=None),
                            arg(arg='previous_operator_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Override to use visitor name instead of 'Visitor' whenever a visitor start a livechat session. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='visitor_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.visitor', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_visitor_from_request',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='visitor_sudo', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='anonymous_name', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='visitor_sudo', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='visitor_sudo', ctx=Load()),
                                                            attr='lang_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        attr='display_name',
                                        ctx=Load(),
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
                                            Name(id='WebsiteLivechat', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_session',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='channel_id', ctx=Load()),
                                    Name(id='anonymous_name', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='previous_operator_id',
                                        value=Name(id='previous_operator_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
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
                            args=[Constant(value='/im_livechat/get_session', kind=None)],
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
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
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
