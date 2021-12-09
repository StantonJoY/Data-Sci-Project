Module(
    body=[
        ImportFrom(
            module='ast',
            names=[alias(name='literal_eval', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='timedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='pytz',
            names=[
                alias(name='timezone', asname=None),
                alias(name='utc', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.exceptions',
            names=[
                alias(name='Forbidden', asname=None),
                alias(name='NotFound', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='babel', asname=None)],
        ),
        Import(
            names=[alias(name='babel.dates', asname=None)],
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='exceptions', asname=None),
                alias(name='http', asname=None),
                alias(name='fields', asname=None),
                alias(name='tools', asname=None),
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
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='is_html_empty', asname=None),
                alias(name='plaintext2html', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='babel_locale_parse', asname=None)],
            level=0,
        ),
        ClassDef(
            name='EventTrackController',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='_get_event_tracks_agenda_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Base domain for displaying track names (preview). The returned search\n        domain will select the tracks that belongs to a track stage that should\n        be visible in the agenda (see: 'is_visible_in_agenda'). Published tracks\n        are also displayed whatever their stage. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='agenda_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='&', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='event_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='|', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='is_published', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='stage_id.is_visible_in_agenda', kind=None),
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
                        Return(
                            value=Name(id='agenda_domain', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_event_tracks_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Base domain for displaying tracks. The returned search domain will\n        select the tracks that belongs to a track stage that should be visible\n        in the agenda (see: 'is_visible_in_agenda'). When the user is a visitor,\n        the domain will contain an additional condition that will remove the\n        unpublished tracks from the search results.", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='search_domain_base', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_event_tracks_agenda_domain',
                                    ctx=Load(),
                                ),
                                args=[Name(id='event', ctx=Load())],
                                keywords=[],
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
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='has_group',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='event.group_event_registration_desk', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='search_domain_base', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='search_domain_base', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='is_published', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=True, kind=None),
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='search_domain_base', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='event_tracks',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='tag', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='searches', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Main route\n\n        :param event: event whose tracks are about to be displayed;\n        :param tag: deprecated: search for a specific tag\n        :param searches: frontend search dict, containing\n\n          * 'search': search string;\n          * 'tags': list of tag IDs for filtering;\n        ", kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_event_track.tracks_session', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_event_tracks_get_values',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='event', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='tag',
                                                value=Name(id='tag', ctx=Load()),
                                            ),
                                            keyword(
                                                arg=None,
                                                value=Name(id='searches', ctx=Load()),
                                            ),
                                        ],
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
                                        Constant(value='/event/<model("event.event"):event>/track', kind=None),
                                        Constant(value='/event/<model("event.event"):event>/track/tag/<model("event.track.tag"):tag>', kind=None),
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
                    name='_event_tracks_get_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='tag', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='searches', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='searches', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='search', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='searches', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='search_wishlist', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='searches', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='tags', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='search_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_event_tracks_agenda_domain',
                                    ctx=Load(),
                                ),
                                args=[Name(id='event', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='searches', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='search', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='search_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='search_domain', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='ilike', kind=None),
                                                                    Subscript(
                                                                        value=Name(id='searches', ctx=Load()),
                                                                        slice=Constant(value='search', kind=None),
                                                                        ctx=Load(),
                                                                    ),
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='search_tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_search_tags',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='searches', ctx=Load()),
                                        slice=Constant(value='tags', kind=None),
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
                                        operand=Name(id='search_tags', ctx=Load()),
                                    ),
                                    Name(id='tag', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='search_tags', ctx=Store())],
                                    value=Name(id='tag', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='search_tags', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='grouped_tags', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='search_tag', ctx=Store()),
                                    iter=Name(id='search_tags', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='grouped_tags', ctx=Load()),
                                                            attr='setdefault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='search_tag', ctx=Load()),
                                                                attr='category_id',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='list', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='search_tag', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='search_domain_items', ctx=Store())],
                                    value=ListComp(
                                        elt=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='tag_ids', kind=None),
                                                        Constant(value='in', kind=None),
                                                        ListComp(
                                                            elt=Attribute(
                                                                value=Name(id='tag', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='tag', ctx=Store()),
                                                                    iter=Subscript(
                                                                        value=Name(id='grouped_tags', ctx=Load()),
                                                                        slice=Name(id='group', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='group', ctx=Store()),
                                                iter=Name(id='grouped_tags', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='search_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='search_domain', ctx=Load()),
                                                    Starred(
                                                        value=Name(id='search_domain_items', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='now_tz', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='utc', ctx=Load()),
                                            attr='localize',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
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
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='microsecond',
                                                        value=Constant(value=0, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='is_dst',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='astimezone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='timezone', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='date_tz',
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
                            targets=[Name(id='today_tz', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='now_tz', ctx=Load()),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tz',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='date_tz',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='UTC', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tracks_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='event.track', kind=None),
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
                                args=[Name(id='search_domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='is_published desc, date asc', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tag_categories', ctx=Store())],
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
                                                slice=Constant(value='event.track.tag.category', kind=None),
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
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='searches', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='search_wishlist', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='tracks_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tracks_sudo', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='track', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='track', ctx=Load()),
                                                    attr='is_reminder_on',
                                                    ctx=Load(),
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
                        Assign(
                            targets=[Name(id='tracks_announced', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tracks_sudo', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='track', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='track', ctx=Load()),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tracks_wdate', ctx=Store())],
                            value=BinOp(
                                left=Name(id='tracks_sudo', ctx=Load()),
                                op=Sub(),
                                right=Name(id='tracks_announced', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_begin_tz_all', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='dt', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='dt', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_get_dt_in_event_tz',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='tracks_wdate', ctx=Load()),
                                                                        attr='mapped',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='date', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                Name(id='event', ctx=Load()),
                                                            ],
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='date_begin_tz_all', ctx=Load()),
                                    attr='sort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tracks_sudo_live', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tracks_wdate', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='track', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='track', ctx=Load()),
                                            attr='is_track_live',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tracks_sudo_soon', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tracks_wdate', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='track', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='track', ctx=Load()),
                                                        attr='is_track_live',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Attribute(
                                                    value=Name(id='track', ctx=Load()),
                                                    attr='is_track_soon',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tracks_by_day', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='display_date', ctx=Store()),
                            iter=Name(id='date_begin_tz_all', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='matching_tracks', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tracks_wdate', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='track', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_get_dt_in_event_tz',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        List(
                                                                            elts=[
                                                                                Attribute(
                                                                                    value=Name(id='track', ctx=Load()),
                                                                                    attr='date',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                        Name(id='event', ctx=Load()),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='date',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='display_date', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tracks_by_day', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='date', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='tracks', kind=None),
                                                ],
                                                values=[
                                                    Name(id='display_date', ctx=Load()),
                                                    Name(id='display_date', ctx=Load()),
                                                    Name(id='matching_tracks', ctx=Load()),
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
                        If(
                            test=Name(id='tracks_announced', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='tracks_announced', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tracks_announced', ctx=Load()),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='wishlisted_by_default', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='reverse',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tracks_by_day', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='date', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='tracks', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Coming soon', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Name(id='tracks_announced', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='tracks_group', ctx=Store()),
                            iter=Name(id='tracks_by_day', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='tracks_group', ctx=Load()),
                                            slice=Constant(value='default_collapsed', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='today_tz', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='tracks_group', ctx=Load()),
                                                        slice=Constant(value='date', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='all', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='track', ctx=Load()),
                                                                    attr='is_track_done',
                                                                    ctx=Load(),
                                                                ),
                                                                UnaryOp(
                                                                    op=Not(),
                                                                    operand=Attribute(
                                                                        value=Name(id='track', ctx=Load()),
                                                                        attr='is_track_live',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='track', ctx=Store()),
                                                                iter=Subscript(
                                                                    value=Name(id='tracks_group', ctx=Load()),
                                                                    slice=Constant(value='tracks', kind=None),
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
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='event', kind=None),
                                    Constant(value='main_object', kind=None),
                                    Constant(value='tracks', kind=None),
                                    Constant(value='tracks_by_day', kind=None),
                                    Constant(value='tracks_live', kind=None),
                                    Constant(value='tracks_soon', kind=None),
                                    Constant(value='today_tz', kind=None),
                                    Constant(value='searches', kind=None),
                                    Constant(value='search_key', kind=None),
                                    Constant(value='search_wishlist', kind=None),
                                    Constant(value='search_tags', kind=None),
                                    Constant(value='tag_categories', kind=None),
                                    Constant(value='is_html_empty', kind=None),
                                    Constant(value='hostname', kind=None),
                                    Constant(value='is_event_user', kind=None),
                                ],
                                values=[
                                    Name(id='event', ctx=Load()),
                                    Name(id='event', ctx=Load()),
                                    Name(id='tracks_sudo', ctx=Load()),
                                    Name(id='tracks_by_day', ctx=Load()),
                                    Name(id='tracks_sudo_live', ctx=Load()),
                                    Name(id='tracks_sudo_soon', ctx=Load()),
                                    Name(id='today_tz', ctx=Load()),
                                    Name(id='searches', ctx=Load()),
                                    Subscript(
                                        value=Name(id='searches', ctx=Load()),
                                        slice=Constant(value='search', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='searches', ctx=Load()),
                                        slice=Constant(value='search_wishlist', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='search_tags', ctx=Load()),
                                    Name(id='tag_categories', ctx=Load()),
                                    Name(id='is_html_empty', ctx=Load()),
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='httprequest',
                                                        ctx=Load(),
                                                    ),
                                                    attr='host',
                                                    ctx=Load(),
                                                ),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=':', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='event.group_event_user', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='event_agenda',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='tag', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tz',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='date_tz',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='UTC', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='event', kind=None),
                                    Constant(value='main_object', kind=None),
                                    Constant(value='tag', kind=None),
                                    Constant(value='is_event_user', kind=None),
                                ],
                                values=[
                                    Name(id='event', ctx=Load()),
                                    Name(id='event', ctx=Load()),
                                    Name(id='tag', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='event.group_event_user', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_calendar_values',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='event', ctx=Load())],
                                        keywords=[],
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
                                    Constant(value='website_event_track.agenda_online', kind=None),
                                    Name(id='vals', ctx=Load()),
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
                                    elts=[Constant(value='/event/<model("event.event"):event>/agenda', kind=None)],
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
                    name='_prepare_calendar_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' This methods slit the day (max end time - min start time) into\n        15 minutes time slots. For each time slot, we assign the tracks that\n        start at this specific time slot, and we add the number of time slot\n        that the track covers (track duration / 15 min). The calendar will be\n        divided into rows of 15 min, and the talks will cover the corresponding\n        number of rows (15 min slots). ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tz',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='date_tz',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='UTC', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='local_tz', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pytz', ctx=Load()),
                                    attr='timezone',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='date_tz',
                                                ctx=Load(),
                                            ),
                                            Constant(value='UTC', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lang_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='lang', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_track_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='AND',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_event_tracks_agenda_domain',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='event', ctx=Load())],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tracks_sudo', ctx=Store())],
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
                                                slice=Constant(value='event.track', kind=None),
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
                                args=[Name(id='base_track_domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='locations', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='track', ctx=Load()),
                                                    attr='location_id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='track', ctx=Store()),
                                                        iter=Name(id='tracks_sudo', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
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
                                    value=Name(id='locations', ctx=Load()),
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
                                                args=[arg(arg='x', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time_slots_by_tracks', ctx=Store())],
                            value=DictComp(
                                key=Name(id='track', ctx=Load()),
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_split_track_by_days',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='track', ctx=Load()),
                                        Name(id='local_tz', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='track', ctx=Store()),
                                        iter=Name(id='tracks_sudo', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='track_time_slots', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='union',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=GeneratorExp(
                                            elt=Call(
                                                func=Attribute(
                                                    value=Name(id='time_slot', ctx=Load()),
                                                    attr='keys',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='time_slot', ctx=Store()),
                                                    iter=ListComp(
                                                        elt=Name(id='time_slots', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='time_slots', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='time_slots_by_tracks', ctx=Load()),
                                                                        attr='values',
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
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='days', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='time_slot', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='time_slot', ctx=Store()),
                                                        iter=Name(id='track_time_slots', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
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
                                    value=Name(id='days', ctx=Load()),
                                    attr='sort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tracks_by_days', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='days', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='time_slots_by_day', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='day', ctx=Load()),
                                                Call(
                                                    func=Name(id='dict', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='start',
                                                            value=Call(
                                                                func=Name(id='set', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        keyword(
                                                            arg='end',
                                                            value=Call(
                                                                func=Name(id='set', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='day', ctx=Store()),
                                                iter=Name(id='days', ctx=Load()),
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
                            targets=[Name(id='tracks_by_rounded_times', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='time_slot', ctx=Load()),
                                                Call(
                                                    func=Name(id='dict', ctx=Load()),
                                                    args=[
                                                        GeneratorExp(
                                                            elt=Tuple(
                                                                elts=[
                                                                    Name(id='location', ctx=Load()),
                                                                    Dict(keys=[], values=[]),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='location', ctx=Store()),
                                                                    iter=Name(id='locations', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='time_slot', ctx=Store()),
                                                iter=Name(id='track_time_slots', ctx=Load()),
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='track', ctx=Store()),
                                    Name(id='time_slots', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='time_slots_by_tracks', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='start_date', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Datetime',
                                                                ctx=Load(),
                                                            ),
                                                            attr='from_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='track', ctx=Load()),
                                                                attr='date',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Name(id='pytz', ctx=Load()),
                                                            attr='utc',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='astimezone',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='local_tz', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='end_date', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='start_date', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='hours',
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='track', ctx=Load()),
                                                                attr='duration',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0.25, kind=None),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='time_slot', ctx=Store()),
                                            Name(id='duration', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='time_slots', ctx=Load()),
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
                                                        value=Subscript(
                                                            value=Name(id='tracks_by_rounded_times', ctx=Load()),
                                                            slice=Name(id='time_slot', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Attribute(
                                                            value=Name(id='track', ctx=Load()),
                                                            attr='location_id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='track', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='rowspan', kind=None),
                                                    Constant(value='start_date', kind=None),
                                                    Constant(value='end_date', kind=None),
                                                    Constant(value='occupied_cells', kind=None),
                                                ],
                                                values=[
                                                    Name(id='duration', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_locale_time',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='start_date', ctx=Load()),
                                                            Name(id='lang_code', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_locale_time',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='end_date', ctx=Load()),
                                                            Name(id='lang_code', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_occupied_cells',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='track', ctx=Load()),
                                                            Name(id='duration', ctx=Load()),
                                                            Name(id='locations', ctx=Load()),
                                                            Name(id='local_tz', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='day', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='time_slot', ctx=Load()),
                                                    attr='date',
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
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='time_slots_by_day', ctx=Load()),
                                                            slice=Name(id='day', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='start', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='time_slot', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='time_slots_by_day', ctx=Load()),
                                                            slice=Name(id='day', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='end', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='time_slot', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='minutes',
                                                                    value=BinOp(
                                                                        left=Constant(value=15, kind=None),
                                                                        op=Mult(),
                                                                        right=Name(id='duration', ctx=Load()),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='tracks_by_days', ctx=Load()),
                                                slice=Name(id='day', ctx=Load()),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
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
                            targets=[Name(id='global_time_slots_by_day', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='day', ctx=Load()),
                                                Dict(keys=[], values=[]),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='day', ctx=Store()),
                                                iter=Name(id='days', ctx=Load()),
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='day', ctx=Store()),
                                    Name(id='time_slots', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='time_slots_by_day', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='start_time_slot', ctx=Store())],
                                    value=Call(
                                        func=Name(id='min', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='time_slots', ctx=Load()),
                                                slice=Constant(value='start', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='end_time_slot', ctx=Store())],
                                    value=Call(
                                        func=Name(id='max', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='time_slots', ctx=Load()),
                                                slice=Constant(value='end', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='time_slots_count', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Name(id='end_time_slot', ctx=Load()),
                                                                op=Sub(),
                                                                right=Name(id='start_time_slot', ctx=Load()),
                                                            ),
                                                            attr='total_seconds',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    op=Div(),
                                                    right=Constant(value=3600, kind=None),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=4, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='current_time_slot', ctx=Store())],
                                    value=Name(id='start_time_slot', ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='i', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            BinOp(
                                                left=Name(id='time_slots_count', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='global_time_slots_by_day', ctx=Load()),
                                                        slice=Name(id='day', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='current_time_slot', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tracks_by_rounded_times', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='current_time_slot', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='global_time_slots_by_day', ctx=Load()),
                                                            slice=Name(id='day', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='current_time_slot', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='formatted_time', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_locale_time',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='current_time_slot', ctx=Load()),
                                                    Name(id='lang_code', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='current_time_slot', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='current_time_slot', ctx=Load()),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='minutes',
                                                            value=Constant(value=15, kind=None),
                                                        ),
                                                    ],
                                                ),
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
                            targets=[Name(id='tracks_by_days', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='days', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='track', ctx=Store()),
                            iter=Name(id='tracks_sudo', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='track_day', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Datetime',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='from_string',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='track', ctx=Load()),
                                                                        attr='date',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='tzinfo',
                                                                value=Attribute(
                                                                    value=Name(id='pytz', ctx=Load()),
                                                                    attr='utc',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='astimezone',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='local_tz', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='tracks_by_days', ctx=Load()),
                                        slice=Name(id='track_day', ctx=Load()),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='days', kind=None),
                                    Constant(value='tracks_by_days', kind=None),
                                    Constant(value='time_slots', kind=None),
                                    Constant(value='locations', kind=None),
                                ],
                                values=[
                                    Name(id='days', ctx=Load()),
                                    Name(id='tracks_by_days', ctx=Load()),
                                    Name(id='global_time_slots_by_day', ctx=Load()),
                                    Name(id='locations', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_locale_time',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='dt_time', annotation=None, type_comment=None),
                            arg(arg='lang_code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Get locale time from datetime object\n\n            :param dt_time: datetime object\n            :param lang_code: language code (eg. en_US)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='locale', ctx=Store())],
                            value=Call(
                                func=Name(id='babel_locale_parse', ctx=Load()),
                                args=[Name(id='lang_code', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='babel', ctx=Load()),
                                        attr='dates',
                                        ctx=Load(),
                                    ),
                                    attr='format_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt_time', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='format',
                                        value=Constant(value='short', kind=None),
                                    ),
                                    keyword(
                                        arg='locale',
                                        value=Name(id='locale', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='time_slot_rounder',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='time', annotation=None, type_comment=None),
                            arg(arg='rounded_minutes', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Rounds to nearest hour by adding a timedelta hour if minute >= rounded_minutes\n            E.g. : If rounded_minutes = 15 -> 09:26:00 becomes 09:30:00\n                                              09:17:00 becomes 09:15:00\n        ', kind=None),
                        ),
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='time', ctx=Load()),
                                        attr='replace',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='second',
                                            value=Constant(value=0, kind=None),
                                        ),
                                        keyword(
                                            arg='microsecond',
                                            value=Constant(value=0, kind=None),
                                        ),
                                        keyword(
                                            arg='minute',
                                            value=Constant(value=0, kind=None),
                                        ),
                                        keyword(
                                            arg='hour',
                                            value=Attribute(
                                                value=Name(id='time', ctx=Load()),
                                                attr='hour',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id='timedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='minutes',
                                            value=BinOp(
                                                left=Name(id='rounded_minutes', ctx=Load()),
                                                op=Mult(),
                                                right=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='time', ctx=Load()),
                                                        attr='minute',
                                                        ctx=Load(),
                                                    ),
                                                    op=FloorDiv(),
                                                    right=Name(id='rounded_minutes', ctx=Load()),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_split_track_by_days',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='track', annotation=None, type_comment=None),
                            arg(arg='local_tz', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Based on the track start_date and the duration,\n        split the track duration into :\n            start_time by day : number of time slot (15 minutes) that the track takes on that day.\n        E.g. :  start date = 01-01-2000 10:00 PM and duration = 3 hours\n                return {\n                    01-01-2000 10:00:00 PM: 8 (2 * 4),\n                    01-02-2000 00:00:00 AM: 4 (1 * 4)\n                }\n        Also return a set of all the time slots\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='start_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='track', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='pytz', ctx=Load()),
                                                    attr='utc',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='astimezone',
                                    ctx=Load(),
                                ),
                                args=[Name(id='local_tz', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start_datetime', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='time_slot_rounder',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start_date', ctx=Load()),
                                    Constant(value=15, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_datetime', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='time_slot_rounder',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='start_datetime', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='hours',
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='track', ctx=Load()),
                                                                attr='duration',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0.25, kind=None),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    Constant(value=15, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='time_slots_count', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=Call(
                                                func=Attribute(
                                                    value=BinOp(
                                                        left=Name(id='end_datetime', ctx=Load()),
                                                        op=Sub(),
                                                        right=Name(id='start_datetime', ctx=Load()),
                                                    ),
                                                    attr='total_seconds',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            op=Div(),
                                            right=Constant(value=3600, kind=None),
                                        ),
                                        op=Mult(),
                                        right=Constant(value=4, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='time_slots_by_day_start_time', ctx=Store())],
                            value=Dict(
                                keys=[Name(id='start_datetime', ctx=Load())],
                                values=[Constant(value=0, kind=None)],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Name(id='time_slots_count', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='next_day', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Name(id='start_datetime', ctx=Load()),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=BinOp(
                                                    left=Name(id='start_datetime', ctx=Load()),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='timedelta', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='minutes',
                                                                value=BinOp(
                                                                    left=Constant(value=15, kind=None),
                                                                    op=Mult(),
                                                                    right=Name(id='i', ctx=Load()),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[LtE()],
                                        comparators=[Name(id='next_day', ctx=Load())],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='time_slots_by_day_start_time', ctx=Load()),
                                                slice=Name(id='start_datetime', ctx=Load()),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='start_datetime', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='next_day', ctx=Load()),
                                                    attr='datetime',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='time_slots_by_day_start_time', ctx=Load()),
                                                    slice=Name(id='start_datetime', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='time_slots_by_day_start_time', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_occupied_cells',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='track', annotation=None, type_comment=None),
                            arg(arg='rowspan', annotation=None, type_comment=None),
                            arg(arg='locations', annotation=None, type_comment=None),
                            arg(arg='local_tz', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        In order to use only once the cells that the tracks will occupy, we need to reserve those cells\n        (time_slot, location) coordinate. Those coordinated will be given to the template to avoid adding\n        blank cells where already occupied by a track.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='occupied_cells', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='track', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='pytz', ctx=Load()),
                                                    attr='utc',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='astimezone',
                                    ctx=Load(),
                                ),
                                args=[Name(id='local_tz', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='time_slot_rounder',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start_date', ctx=Load()),
                                    Constant(value=15, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Name(id='rowspan', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='time_slot', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='start_date', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='minutes',
                                                    value=BinOp(
                                                        left=Constant(value=15, kind=None),
                                                        op=Mult(),
                                                        right=Name(id='i', ctx=Load()),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='track', ctx=Load()),
                                        attr='location_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='occupied_cells', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='time_slot', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='track', ctx=Load()),
                                                                attr='location_id',
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
                                    orelse=[
                                        AugAssign(
                                            target=Name(id='occupied_cells', ctx=Store()),
                                            op=Add(),
                                            value=ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Name(id='time_slot', ctx=Load()),
                                                        Name(id='location', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='location', ctx=Store()),
                                                        iter=Name(id='locations', ctx=Load()),
                                                        ifs=[Name(id='location', ctx=Load())],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='occupied_cells', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='event_track_page',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='track', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='options', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='track', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fetch_track',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='track', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='allow_sudo',
                                        value=Constant(value=False, kind=None),
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
                                    Constant(value='website_event_track.event_track_main', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_event_track_page_get_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='event', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='track', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='options', ctx=Load()),
                                            ),
                                        ],
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
                            args=[Constant(value='/event/<model("event.event", "[(\'website_track\', \'=\', True)]"):event>/track/<model("event.track", "[(\'event_id\', \'=\', event.id)]"):track>', kind=None)],
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
                    name='_event_track_page_get_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='track', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='options', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='track', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='track', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='option_widescreen', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='widescreen', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='option_widescreen', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='option_widescreen', ctx=Load()),
                                    ops=[NotEq()],
                                    comparators=[Constant(value='0', kind=None)],
                                ),
                                body=Call(
                                    func=Name(id='bool', ctx=Load()),
                                    args=[Name(id='option_widescreen', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tracks_other', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='track', ctx=Load()),
                                    attr='_get_track_suggestions',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='restrict_domain',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_event_tracks_domain',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='track', ctx=Load()),
                                                    attr='event_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=10, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='event', kind=None),
                                    Constant(value='main_object', kind=None),
                                    Constant(value='track', kind=None),
                                    Constant(value='tracks_other', kind=None),
                                    Constant(value='option_widescreen', kind=None),
                                    Constant(value='is_html_empty', kind=None),
                                    Constant(value='hostname', kind=None),
                                    Constant(value='is_event_user', kind=None),
                                ],
                                values=[
                                    Name(id='event', ctx=Load()),
                                    Name(id='track', ctx=Load()),
                                    Name(id='track', ctx=Load()),
                                    Name(id='tracks_other', ctx=Load()),
                                    Name(id='option_widescreen', ctx=Load()),
                                    Name(id='is_html_empty', ctx=Load()),
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='httprequest',
                                                        ctx=Load(),
                                                    ),
                                                    attr='host',
                                                    ctx=Load(),
                                                ),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=':', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='event.group_event_user', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='track_reminder_toggle',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='track_id', annotation=None, type_comment=None),
                            arg(arg='set_reminder_on', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Set a reminder a track for current visitor. Track visitor is created or updated\n        if it already exists. Exception made if un-favoriting and no track_visitor\n        record found (should not happen unless manually done).\n\n        :param boolean set_reminder_on:\n          If True, set as a favorite, otherwise un-favorite track;\n          If the track is a Key Track (wishlisted_by_default):\n            if set_reminder_on = False, blacklist the track_partner\n            otherwise, un-blacklist the track_partner\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='track', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fetch_track',
                                    ctx=Load(),
                                ),
                                args=[Name(id='track_id', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='allow_sudo',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='force_create', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='set_reminder_on', ctx=Load()),
                                    Attribute(
                                        value=Name(id='track', ctx=Load()),
                                        attr='wishlisted_by_default',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event_track_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='track', ctx=Load()),
                                    attr='_get_event_track_visitors',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='force_create',
                                        value=Name(id='force_create', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='visitor_sudo', ctx=Store())],
                            value=Attribute(
                                value=Name(id='event_track_partner', ctx=Load()),
                                attr='visitor_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='track', ctx=Load()),
                                    attr='wishlisted_by_default',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='event_track_partner', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='event_track_partner', ctx=Load()),
                                                    attr='is_wishlisted',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='set_reminder_on', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='error', kind=None)],
                                                values=[Constant(value='ignored', kind=None)],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='event_track_partner', ctx=Load()),
                                            attr='is_wishlisted',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='set_reminder_on', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='event_track_partner', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='event_track_partner', ctx=Load()),
                                                    attr='is_blacklisted',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Name(id='set_reminder_on', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='error', kind=None)],
                                                values=[Constant(value='ignored', kind=None)],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='event_track_partner', ctx=Load()),
                                            attr='is_blacklisted',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='set_reminder_on', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='reminderOn', kind=None)],
                                values=[Name(id='set_reminder_on', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
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
                                        Constant(value='visitor_uuid', kind=None),
                                        Constant(value='', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='visitor_sudo', ctx=Load()),
                                        attr='access_token',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='visitor_uuid', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='visitor_sudo', ctx=Load()),
                                        attr='access_token',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/event/track/toggle_reminder', kind=None)],
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
                    name='event_track_proposal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
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
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_event_track.event_track_proposal', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='event', kind=None),
                                            Constant(value='main_object', kind=None),
                                        ],
                                        values=[
                                            Name(id='event', ctx=Load()),
                                            Name(id='event', ctx=Load()),
                                        ],
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
                                    elts=[Constant(value='/event/<model("event.event"):event>/track_proposal', kind=None)],
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
                    name='event_track_proposal_post',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
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
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='can_access_from_current_website',
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
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='error', kind=None)],
                                                values=[Constant(value='forbidden', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='input_tag_indices', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[Name(id='tag_id', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='tag_id', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='post', ctx=Load()),
                                                    slice=Constant(value='tags', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=',', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[Name(id='tag_id', ctx=Load())],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='valid_tag_indices', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='event.track.tag', kind=None),
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
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Name(id='input_tag_indices', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contact', ctx=Store())],
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
                            targets=[Name(id='visitor_partner', ctx=Store())],
                            value=Attribute(
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
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='add_contact_information', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='valid_contact_email', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='email_normalize',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='post', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='contact_email', kind=None)],
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
                                            Name(id='valid_contact_email', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='post', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='contact_phone', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='visitor_partner', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='valid_contact_email', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='visitor_partner', ctx=Load()),
                                                                attr='email_normalized',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='contact', ctx=Store())],
                                                    value=Name(id='visitor_partner', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='contact', ctx=Store())],
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
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='email', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='phone', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='valid_contact_email', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='post', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='contact_name', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='post', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='contact_phone', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='json', ctx=Load()),
                                                    attr='dumps',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='error', kind=None)],
                                                        values=[Constant(value='invalidFormInputs', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='valid_speaker_email', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='email_normalize',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='post', ctx=Load()),
                                                slice=Constant(value='partner_email', kind=None),
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
                                            Name(id='visitor_partner', ctx=Load()),
                                            Compare(
                                                left=Name(id='valid_speaker_email', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='visitor_partner', ctx=Load()),
                                                        attr='email_normalized',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='contact', ctx=Store())],
                                            value=Name(id='visitor_partner', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='track', ctx=Store())],
                            value=Call(
                                func=Attribute(
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
                                                        slice=Constant(value='event.track', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='mail_create_nosubscribe', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='partner_name', kind=None),
                                            Constant(value='partner_email', kind=None),
                                            Constant(value='partner_phone', kind=None),
                                            Constant(value='partner_function', kind=None),
                                            Constant(value='contact_phone', kind=None),
                                            Constant(value='contact_email', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='tag_ids', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='partner_biography', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='image', kind=None),
                                        ],
                                        values=[
                                            Subscript(
                                                value=Name(id='post', ctx=Load()),
                                                slice=Constant(value='track_name', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='contact', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='post', ctx=Load()),
                                                slice=Constant(value='partner_name', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='post', ctx=Load()),
                                                slice=Constant(value='partner_email', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='post', ctx=Load()),
                                                slice=Constant(value='partner_phone', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='post', ctx=Load()),
                                                slice=Constant(value='partner_function', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='contact', ctx=Load()),
                                                attr='phone',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='contact', ctx=Load()),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Name(id='valid_tag_indices', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='plaintext2html', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='post', ctx=Load()),
                                                        slice=Constant(value='description', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='plaintext2html', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='post', ctx=Load()),
                                                        slice=Constant(value='partner_biography', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                            IfExp(
                                                test=Call(
                                                    func=Attribute(
                                                        value=Name(id='post', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='image', kind=None)],
                                                    keywords=[],
                                                ),
                                                body=Call(
                                                    func=Attribute(
                                                        value=Name(id='base64', ctx=Load()),
                                                        attr='b64encode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='post', ctx=Load()),
                                                                    slice=Constant(value='image', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='read',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                orelse=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='website',
                                            ctx=Load(),
                                        ),
                                        attr='user_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='track', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='message_subscribe',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_ids',
                                                value=Attribute(
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
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='success', kind=None)],
                                        values=[Constant(value=True, kind=None)],
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
                                    elts=[Constant(value='/event/<model("event.event"):event>/track_proposal/post', kind=None)],
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
                    name='website_event_track_fetch_tags',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='event.track.tag', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
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
                                    elts=[Constant(value='/event/track_tag/search_read', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
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
                    name='_fetch_track',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='track_id', annotation=None, type_comment=None),
                            arg(arg='allow_sudo', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='track', ctx=Store())],
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
                                                slice=Constant(value='event.track', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='track_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='exists',
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
                                operand=Name(id='track', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='NotFound', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='track', ctx=Load()),
                                            attr='check_access_rights',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='read', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='track', ctx=Load()),
                                            attr='check_access_rule',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='read', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='exceptions', ctx=Load()),
                                        attr='AccessError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='allow_sudo', ctx=Load()),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='Forbidden', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='track', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='track', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
                            value=Attribute(
                                value=Name(id='track', ctx=Load()),
                                attr='event_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='request', ctx=Load()),
                                            Constant(value='website_id', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='can_access_from_current_website',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='NotFound', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='check_access_rights',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='read', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='check_access_rule',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='read', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='exceptions', ctx=Load()),
                                        attr='AccessError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Forbidden', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='track', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_search_tags',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tag_search', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='tag_ids', ctx=Store())],
                                    value=Call(
                                        func=Name(id='literal_eval', ctx=Load()),
                                        args=[Name(id='tag_search', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
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
                                                        slice=Constant(value='event.track.tag', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='tags', ctx=Store())],
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
                                                        slice=Constant(value='event.track.tag', kind=None),
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
                                                            Constant(value='in', kind=None),
                                                            Name(id='tag_ids', ctx=Load()),
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
                            ],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='tags', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_dt_in_event_tz',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='datetimes', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='tz_name', ctx=Store())],
                            value=Attribute(
                                value=Name(id='event', ctx=Load()),
                                attr='date_tz',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='utc', ctx=Load()),
                                                attr='localize',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='dt', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='is_dst',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='astimezone',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='timezone', ctx=Load()),
                                            args=[Name(id='tz_name', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='dt', ctx=Store()),
                                        iter=Name(id='datetimes', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
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
