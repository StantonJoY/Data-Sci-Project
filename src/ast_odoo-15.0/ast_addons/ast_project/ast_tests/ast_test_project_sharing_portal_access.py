Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='OrderedDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='Command', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='test_project_sharing',
            names=[alias(name='TestProjectSharingCommon', asname=None)],
            level=1,
        ),
        ClassDef(
            name='TestProjectSharingPortalAccess',
            bases=[Name(id='TestProjectSharingCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_share_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.share.wizard', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='access_mode', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='partner_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='edit', kind=None),
                                            Constant(value='project.project', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='project_portal',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='link',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='partner_portal',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='project_share_wizard', ctx=Load()),
                                    attr='action_send_mail',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Task', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='project.task', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='read_protected_fields_task',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='OrderedDict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='k', ctx=Load()),
                                                Name(id='v', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='k', ctx=Store()),
                                                        Name(id='v', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='Task', ctx=Load()),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='k', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='Task', ctx=Load()),
                                                                attr='SELF_READABLE_FIELDS',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='write_protected_fields_task',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='OrderedDict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='k', ctx=Load()),
                                                Name(id='v', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='k', ctx=Store()),
                                                        Name(id='v', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='Task', ctx=Load()),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='k', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='Task', ctx=Load()),
                                                                attr='SELF_WRITABLE_FIELDS',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='readonly_protected_fields_task',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='OrderedDict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='k', ctx=Load()),
                                                Name(id='v', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='k', ctx=Store()),
                                                        Name(id='v', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='Task', ctx=Load()),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='k', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='Task', ctx=Load()),
                                                                        attr='SELF_READABLE_FIELDS',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Compare(
                                                                left=Name(id='k', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='Task', ctx=Load()),
                                                                        attr='SELF_WRITABLE_FIELDS',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='other_fields_task',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='OrderedDict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='k', ctx=Load()),
                                                Name(id='v', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='k', ctx=Store()),
                                                        Name(id='v', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='Task', ctx=Load()),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='k', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='Task', ctx=Load()),
                                                                attr='SELF_READABLE_FIELDS',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_readonly_fields',
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
                            value=Constant(value=' The fields are not writeable should not be editable by the portal user. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='view_infos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='task_portal',
                                        ctx=Load(),
                                    ),
                                    attr='fields_view_get',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='view_id',
                                        value=Attribute(
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
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='project_sharing_form_view_xml_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                        Assign(
                            targets=[Name(id='project_task_fields', ctx=Store())],
                            value=SetComp(
                                elt=Name(id='field_name', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='field_name', ctx=Store()),
                                                Name(id='field_attrs', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='view_infos', ctx=Load()),
                                                    slice=Constant(value='fields', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Compare(
                                                left=Name(id='field_name', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='write_protected_fields_task',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_project_sharing_form_view',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='task_portal',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='form', ctx=Store()),
                                ),
                            ],
                            body=[
                                For(
                                    target=Name(id='field', ctx=Store()),
                                    iter=Name(id='project_task_fields', ctx=Load()),
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertRaises',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='AssertionError', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='msg',
                                                                value=Constant(value="Field '%s' should be readonly in the project sharing form view ", kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    optional_vars=None,
                                                ),
                                            ],
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='form', ctx=Load()),
                                                            attr='__setattr__',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='field', ctx=Load()),
                                                            Constant(value='coucou', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_read_task_with_portal_user',
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
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='task_portal',
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='read_protected_fields_task',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AccessError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_portal',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_portal',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='other_fields_task',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_write_with_portal_user',
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
                            target=Name(id='field', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='readonly_protected_fields_task',
                                ctx=Load(),
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertRaises',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='AccessError', ctx=Load())],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='task_portal',
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_user',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='user_portal',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Name(id='field', ctx=Load())],
                                                        values=[Constant(value='dummy', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='field', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='other_fields_task',
                                ctx=Load(),
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertRaises',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='AccessError', ctx=Load())],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='task_portal',
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_user',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='user_portal',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Name(id='field', ctx=Load())],
                                                        values=[Constant(value='dummy', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
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
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
