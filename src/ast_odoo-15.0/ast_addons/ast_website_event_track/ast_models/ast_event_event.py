Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='slug', asname=None)],
            level=0,
        ),
        ClassDef(
            name='Event',
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
                    value=Constant(value='event.event', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='track_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='event.track', kind=None),
                            Constant(value='event_id', kind=None),
                            Constant(value='Tracks', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='track_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Track Count', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_track_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='website_track', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Tracks on Website', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_website_track', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='website_track_proposal', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Proposals on Website', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_website_track_proposal', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='track_menu_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='website.event.menu', kind=None),
                            Constant(value='event_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Event Tracks Menus', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='menu_type', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value='track', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='track_proposal_menu_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='website.event.menu', kind=None),
                            Constant(value='event_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Event Proposals Menus', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='menu_type', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value='track_proposal', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='allowed_track_tag_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='event.track.tag', kind=None)],
                        keywords=[
                            keyword(
                                arg='relation',
                                value=Constant(value='event_allowed_track_tags_rel', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Available Track Tags', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tracks_tag_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='event.track.tag', kind=None)],
                        keywords=[
                            keyword(
                                arg='relation',
                                value=Constant(value='event_track_tags_rel', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Track Tags', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_tracks_tag_ids', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_track_count',
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
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='event.track', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='stage_id.is_cancel', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='event_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='event_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='event_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='data', ctx=Load()),
                                                    slice=Constant(value='event_id_count', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='data', ctx=Store()),
                                                iter=Name(id='data', ctx=Load()),
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
                            target=Name(id='event', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='track_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_website_track',
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
                            value=Constant(value=' Propagate event_type configuration (only at change); otherwise propagate\n        website_menu updated value. Also force True is track_proposal changes. ', kind=None),
                        ),
                        For(
                            target=Name(id='event', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='event_type_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='event_type_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='_origin',
                                                            ctx=Load(),
                                                        ),
                                                        attr='event_type_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='website_track',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='event_type_id',
                                                    ctx=Load(),
                                                ),
                                                attr='website_track',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='website_menu',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='event', ctx=Load()),
                                                                    attr='website_menu',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='event', ctx=Load()),
                                                                            attr='_origin',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='website_menu',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='event', ctx=Load()),
                                                                    attr='website_track',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='website_track',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='website_menu',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='event', ctx=Load()),
                                                                    attr='website_track',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=False, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
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
                            args=[
                                Constant(value='event_type_id', kind=None),
                                Constant(value='website_menu', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_website_track_proposal',
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
                            value=Constant(value=' Propagate event_type configuration (only at change); otherwise propagate\n        website_track updated value (both together True or False at update). ', kind=None),
                        ),
                        For(
                            target=Name(id='event', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='event_type_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='event_type_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='_origin',
                                                            ctx=Load(),
                                                        ),
                                                        attr='event_type_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='website_track_proposal',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='event_type_id',
                                                    ctx=Load(),
                                                ),
                                                attr='website_track_proposal',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='website_track',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='event', ctx=Load()),
                                                                    attr='_origin',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='website_track',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='website_track',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='website_track_proposal',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='website_track_proposal',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='website_track',
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='event_type_id', kind=None),
                                Constant(value='website_track', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_tracks_tag_ids',
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
                            target=Name(id='event', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='tracks_tag_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='track_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='tag_ids', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='tag', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Name(id='tag', ctx=Load()),
                                                            attr='color',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
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
                            args=[
                                Constant(value='track_ids.tag_ids', kind=None),
                                Constant(value='track_ids.tag_ids.color', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='toggle_website_track',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='val', annotation=None, type_comment=None),
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
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='website_track',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='val', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='toggle_website_track_proposal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='val', annotation=None, type_comment=None),
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
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='website_track_proposal',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='val', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_menu_update_fields',
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
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[
                                                Name(id='Event', ctx=Load()),
                                                Name(id='self', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='_get_menu_update_fields',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Constant(value='website_track', kind=None),
                                        Constant(value='website_track_proposal', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_website_menus',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='menus_update_by_field', annotation=None, type_comment=None),
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
                                        args=[
                                            Name(id='Event', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_update_website_menus',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='menus_update_by_field',
                                        value=Name(id='menus_update_by_field', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        For(
                            target=Name(id='event', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='menu_id',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='menus_update_by_field', ctx=Load()),
                                                    ),
                                                    Compare(
                                                        left=Name(id='event', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='menus_update_by_field', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='website_track', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='_update_website_menu_entry',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='website_track', kind=None),
                                                    Constant(value='track_menu_ids', kind=None),
                                                    Constant(value='track', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='menu_id',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='menus_update_by_field', ctx=Load()),
                                                    ),
                                                    Compare(
                                                        left=Name(id='event', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='menus_update_by_field', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='website_track_proposal', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='_update_website_menu_entry',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='website_track_proposal', kind=None),
                                                    Constant(value='track_proposal_menu_ids', kind=None),
                                                    Constant(value='track_proposal', kind=None),
                                                ],
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_menu_type_field_matching',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Event', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_menu_type_field_matching',
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
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='track_proposal', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='website_track_proposal', kind=None),
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
                    name='_get_website_menu_entries',
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
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[
                                                Name(id='Event', ctx=Load()),
                                                Name(id='self', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='_get_website_menu_entries',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Talks', kind=None)],
                                                    keywords=[],
                                                ),
                                                BinOp(
                                                    left=Constant(value='/event/%s/track', kind=None),
                                                    op=Mod(),
                                                    right=Call(
                                                        func=Name(id='slug', ctx=Load()),
                                                        args=[Name(id='self', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Constant(value=False, kind=None),
                                                Constant(value=10, kind=None),
                                                Constant(value='track', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Agenda', kind=None)],
                                                    keywords=[],
                                                ),
                                                BinOp(
                                                    left=Constant(value='/event/%s/agenda', kind=None),
                                                    op=Mod(),
                                                    right=Call(
                                                        func=Name(id='slug', ctx=Load()),
                                                        args=[Name(id='self', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Constant(value=False, kind=None),
                                                Constant(value=70, kind=None),
                                                Constant(value='track', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Talk Proposals', kind=None)],
                                                    keywords=[],
                                                ),
                                                BinOp(
                                                    left=Constant(value='/event/%s/track_proposal', kind=None),
                                                    op=Mod(),
                                                    right=Call(
                                                        func=Name(id='slug', ctx=Load()),
                                                        args=[Name(id='self', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Constant(value=False, kind=None),
                                                Constant(value=15, kind=None),
                                                Constant(value='track_proposal', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
