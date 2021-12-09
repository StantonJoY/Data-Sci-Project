Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
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
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='AccountMove',
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
                    value=Constant(value='account.move', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='edi_document_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='account.edi.document', kind=None),
                            ),
                            keyword(
                                arg='inverse_name',
                                value=Constant(value='move_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='edi_state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='to_send', kind=None),
                                                Constant(value='To Send', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='sent', kind=None),
                                                Constant(value='Sent', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='to_cancel', kind=None),
                                                Constant(value='To Cancel', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='cancelled', kind=None),
                                                Constant(value='Cancelled', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Electronic invoicing', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_edi_state', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The aggregated state of all the EDIs with web-service of this move', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='edi_error_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_edi_error_count', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='How many EDIs are in error for this move ?', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='edi_blocking_level', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='info', kind=None),
                                                Constant(value='Info', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='warning', kind=None),
                                                Constant(value='Warning', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='error', kind=None),
                                                Constant(value='Error', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_edi_error_message', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='edi_error_message', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_edi_error_message', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='edi_web_services_to_process', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_edi_web_services_to_process', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Technical field to display the documents that will be processed by the CRON', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='edi_show_cancel_button', ctx=Store())],
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
                                value=Constant(value='_compute_edi_show_cancel_button', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='edi_show_abandon_cancel_button', ctx=Store())],
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
                                value=Constant(value='_compute_edi_show_abandon_cancel_button', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_edi_state',
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
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='all_states', ctx=Store())],
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='edi_document_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='d', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='d', ctx=Load()),
                                                                            attr='edi_format_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='_needs_web_services',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='state', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='all_states', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[
                                            Set(
                                                elts=[Constant(value='sent', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='edi_state',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='sent', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='all_states', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Set(
                                                        elts=[Constant(value='cancelled', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='edi_state',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='cancelled', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Constant(value='to_send', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='all_states', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='edi_state',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='to_send', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Constant(value='to_cancel', kind=None),
                                                                ops=[In()],
                                                                comparators=[Name(id='all_states', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='edi_state',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='to_cancel', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='edi_state',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value=False, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
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
                            args=[Constant(value='edi_document_ids.state', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_edi_error_count',
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
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='edi_error_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='edi_document_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='d', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Attribute(
                                                            value=Name(id='d', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
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
                            args=[Constant(value='edi_document_ids.error', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_edi_error_message',
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
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='edi_error_count',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='edi_error_message',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='edi_blocking_level',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='edi_error_count',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='error_doc', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='edi_document_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='d', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Attribute(
                                                                    value=Name(id='d', ctx=Load()),
                                                                    attr='error',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='edi_error_message',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='error_doc', ctx=Load()),
                                                        attr='error',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='edi_blocking_level',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='error_doc', ctx=Load()),
                                                        attr='blocking_level',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='error_levels', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[
                                                            ListComp(
                                                                elt=Attribute(
                                                                    value=Name(id='doc', ctx=Load()),
                                                                    attr='blocking_level',
                                                                    ctx=Load(),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='doc', ctx=Store()),
                                                                        iter=Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='edi_document_ids',
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
                                                If(
                                                    test=Compare(
                                                        left=Constant(value='error', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='error_levels', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='edi_error_message',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='edi_error_count',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value=' Electronic invoicing error(s)', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='edi_blocking_level',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='error', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Constant(value='warning', kind=None),
                                                                ops=[In()],
                                                                comparators=[Name(id='error_levels', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='edi_error_message',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=BinOp(
                                                                        left=Call(
                                                                            func=Name(id='str', ctx=Load()),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='move', ctx=Load()),
                                                                                    attr='edi_error_count',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value=' Electronic invoicing warning(s)', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='edi_blocking_level',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='warning', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='edi_error_message',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=BinOp(
                                                                        left=Call(
                                                                            func=Name(id='str', ctx=Load()),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='move', ctx=Load()),
                                                                                    attr='edi_error_count',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value=' Electronic invoicing info(s)', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='edi_blocking_level',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='info', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
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
                                Constant(value='edi_error_count', kind=None),
                                Constant(value='edi_document_ids.error', kind=None),
                                Constant(value='edi_document_ids.blocking_level', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_edi_web_services_to_process',
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
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='to_process', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='edi_document_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='d', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='d', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[In()],
                                                            comparators=[
                                                                List(
                                                                    elts=[
                                                                        Constant(value='to_send', kind=None),
                                                                        Constant(value='to_cancel', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='d', ctx=Load()),
                                                                attr='blocking_level',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[NotEq()],
                                                            comparators=[Constant(value='error', kind=None)],
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
                                    targets=[Name(id='format_web_services', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='to_process', ctx=Load()),
                                                attr='edi_format_id',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='f', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Call(
                                                    func=Attribute(
                                                        value=Name(id='f', ctx=Load()),
                                                        attr='_needs_web_services',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='edi_web_services_to_process',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value=', ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='f', ctx=Store()),
                                                        iter=Name(id='format_web_services', ctx=Load()),
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
                                Constant(value='edi_document_ids', kind=None),
                                Constant(value='edi_document_ids.state', kind=None),
                                Constant(value='edi_document_ids.blocking_level', kind=None),
                                Constant(value='edi_document_ids.edi_format_id', kind=None),
                                Constant(value='edi_document_ids.edi_format_id.name', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_show_reset_to_draft_button',
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
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compute_show_reset_to_draft_button',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='doc', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='doc', ctx=Load()),
                                                                attr='edi_format_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_needs_web_services',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='doc', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='sent', kind=None),
                                                                    Constant(value='to_cancel', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='is_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='include_receipts',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='doc', ctx=Load()),
                                                                attr='edi_format_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_is_required_for_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='move', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='show_reset_to_draft_button',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=False, kind=None),
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
                                Constant(value='state', kind=None),
                                Constant(value='edi_document_ids.state', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_edi_show_cancel_button',
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
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='posted', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='edi_show_cancel_button',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='edi_show_cancel_button',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='doc', ctx=Load()),
                                                                    attr='edi_format_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_needs_web_services',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='doc', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='sent', kind=None)],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='is_invoice',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='include_receipts',
                                                                    value=Constant(value=True, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='doc', ctx=Load()),
                                                                    attr='edi_format_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_is_required_for_invoice',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='move', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='doc', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='edi_document_ids',
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
                                Constant(value='state', kind=None),
                                Constant(value='edi_document_ids.state', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_edi_show_abandon_cancel_button',
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
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='edi_show_abandon_cancel_button',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='doc', ctx=Load()),
                                                                    attr='edi_format_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_needs_web_services',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='doc', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='to_cancel', kind=None)],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='is_invoice',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='include_receipts',
                                                                    value=Constant(value=True, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='doc', ctx=Load()),
                                                                    attr='edi_format_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_is_required_for_invoice',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='move', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='doc', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='edi_document_ids',
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
                                Constant(value='state', kind=None),
                                Constant(value='edi_document_ids.state', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_edi_tax_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='results', annotation=None, type_comment=None),
                            arg(arg='grouping_key', annotation=None, type_comment=None),
                            arg(arg='serialized_grouping_key', annotation=None, type_comment=None),
                            arg(arg='tax_values', annotation=None, type_comment=None),
                            arg(arg='key_by_tax', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        AugAssign(
                            target=Subscript(
                                value=Name(id='results', ctx=Load()),
                                slice=Constant(value='tax_amount', kind=None),
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Subscript(
                                value=Name(id='tax_values', ctx=Load()),
                                slice=Constant(value='tax_amount', kind=None),
                                ctx=Load(),
                            ),
                        ),
                        AugAssign(
                            target=Subscript(
                                value=Name(id='results', ctx=Load()),
                                slice=Constant(value='tax_amount_currency', kind=None),
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Subscript(
                                value=Name(id='tax_values', ctx=Load()),
                                slice=Constant(value='tax_amount_currency', kind=None),
                                ctx=Load(),
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='serialized_grouping_key', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='tax_details', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='tax_details', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='results', ctx=Load()),
                                            slice=Constant(value='tax_details', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='serialized_grouping_key', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tax_details', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='grouping_key', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tax_details', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='base_amount', kind=None),
                                                    Constant(value='base_amount_currency', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='tax_values', ctx=Load()),
                                                        slice=Constant(value='base_amount', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='tax_values', ctx=Load()),
                                                        slice=Constant(value='base_amount_currency', kind=None),
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
                                    targets=[Name(id='tax_details', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='results', ctx=Load()),
                                            slice=Constant(value='tax_details', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='serialized_grouping_key', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='key_by_tax', ctx=Load()),
                                            slice=Subscript(
                                                value=Name(id='tax_values', ctx=Load()),
                                                slice=Constant(value='tax_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='key_by_tax', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='tax_values', ctx=Load()),
                                                            slice=Constant(value='src_line_id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='tax_line_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='tax_details', ctx=Load()),
                                                slice=Constant(value='base_amount', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Subscript(
                                                value=Name(id='tax_values', ctx=Load()),
                                                slice=Constant(value='base_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='tax_details', ctx=Load()),
                                                slice=Constant(value='base_amount_currency', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Subscript(
                                                value=Name(id='tax_values', ctx=Load()),
                                                slice=Constant(value='base_amount_currency', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        AugAssign(
                            target=Subscript(
                                value=Name(id='tax_details', ctx=Load()),
                                slice=Constant(value='tax_amount', kind=None),
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Subscript(
                                value=Name(id='tax_values', ctx=Load()),
                                slice=Constant(value='tax_amount', kind=None),
                                ctx=Load(),
                            ),
                        ),
                        AugAssign(
                            target=Subscript(
                                value=Name(id='tax_details', ctx=Load()),
                                slice=Constant(value='tax_amount_currency', kind=None),
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Subscript(
                                value=Name(id='tax_values', ctx=Load()),
                                slice=Constant(value='tax_amount_currency', kind=None),
                                ctx=Load(),
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='tax_details', ctx=Load()),
                                        slice=Constant(value='group_tax_details', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tax_values', ctx=Load())],
                                keywords=[],
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
                    name='_prepare_edi_tax_details',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filter_to_apply', annotation=None, type_comment=None),
                            arg(arg='filter_invl_to_apply', annotation=None, type_comment=None),
                            arg(arg='grouping_key_generator', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Compute amounts related to taxes for the current invoice.\n\n        :param filter_to_apply:         Optional filter to exclude some tax values from the final results.\n                                        The filter is defined as a method getting a dictionary as parameter\n                                        representing the tax values for a single repartition line.\n                                        This dictionary contains:\n\n            'base_line_id':             An account.move.line record.\n            'tax_id':                   An account.tax record.\n            'tax_repartition_line_id':  An account.tax.repartition.line record.\n            'base_amount':              The tax base amount expressed in company currency.\n            'tax_amount':               The tax amount expressed in company currency.\n            'base_amount_currency':     The tax base amount expressed in foreign currency.\n            'tax_amount_currency':      The tax amount expressed in foreign currency.\n\n                                        If the filter is returning False, it means the current tax values will be\n                                        ignored when computing the final results.\n\n        :param filter_invl_to_apply:    Optional filter to exclude some invoice lines.\n\n        :param grouping_key_generator:  Optional method used to group tax values together. By default, the tax values\n                                        are grouped by tax. This parameter is a method getting a dictionary as parameter\n                                        (same signature as 'filter_to_apply').\n\n                                        This method must returns a dictionary where values will be used to create the\n                                        grouping_key to aggregate tax values together. The returned dictionary is added\n                                        to each tax details in order to retrieve the full grouping_key later.\n\n        :return:                        The full tax details for the current invoice and for each invoice line\n                                        separately. The returned dictionary is the following:\n\n            'base_amount':              The total tax base amount in company currency for the whole invoice.\n            'tax_amount':               The total tax amount in company currency for the whole invoice.\n            'base_amount_currency':     The total tax base amount in foreign currency for the whole invoice.\n            'tax_amount_currency':      The total tax amount in foreign currency for the whole invoice.\n            'tax_details':              A mapping of each grouping key (see 'grouping_key_generator') to a dictionary\n                                        containing:\n\n                'base_amount':              The tax base amount in company currency for the current group.\n                'tax_amount':               The tax amount in company currency for the current group.\n                'base_amount_currency':     The tax base amount in foreign currency for the current group.\n                'tax_amount_currency':      The tax amount in foreign currency for the current group.\n                'group_tax_details':        The list of all tax values aggregated into this group.\n\n            'invoice_line_tax_details': A mapping of each invoice line to a dictionary containing:\n\n                'base_amount':          The total tax base amount in company currency for the whole invoice line.\n                'tax_amount':           The total tax amount in company currency for the whole invoice line.\n                'base_amount_currency': The total tax base amount in foreign currency for the whole invoice line.\n                'tax_amount_currency':  The total tax amount in foreign currency for the whole invoice line.\n                'tax_details':          A mapping of each grouping key (see 'grouping_key_generator') to a dictionary\n                                        containing:\n\n                    'base_amount':          The tax base amount in company currency for the current group.\n                    'tax_amount':           The tax amount in company currency for the current group.\n                    'base_amount_currency': The tax base amount in foreign currency for the current group.\n                    'tax_amount_currency':  The tax amount in foreign currency for the current group.\n                    'group_tax_details':    The list of all tax values aggregated into this group.\n\n        ", kind=None),
                        ),
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
                        FunctionDef(
                            name='_serialize_python_dictionary',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='vals', annotation=None, type_comment=None)],
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
                                            value=Constant(value='-', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='vals', ctx=Load()),
                                                            slice=Name(id='k', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='k', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='sorted', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='vals', ctx=Load()),
                                                                        attr='keys',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
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
                            name='default_grouping_key_generator',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='tax_values', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='tax', kind=None)],
                                        values=[
                                            Subscript(
                                                value=Name(id='tax_values', ctx=Load()),
                                                slice=Constant(value='tax_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice_line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='display_type',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='filter_invl_to_apply', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='invoice_lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='invoice_lines', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='filter_invl_to_apply', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='invoice_lines_tax_values_dict', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
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
                                            Constant(value='move_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
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
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='tax_details_query', ctx=Store()),
                                        Name(id='tax_details_params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_lines', ctx=Load()),
                                    attr='_get_query_tax_details_from_domain',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tax_details_query', ctx=Load()),
                                    Name(id='tax_details_params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='dictfetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='invoice_line', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='invoice_lines', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='base_line_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tax_line', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='invoice_lines', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='tax_line_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='src_line', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='invoice_lines', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='src_line_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tax', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='tax_id', kind=None),
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
                                            value=Subscript(
                                                value=Name(id='invoice_lines_tax_values_dict', ctx=Load()),
                                                slice=Name(id='invoice_line', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='base_line_id', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='src_line_id', kind=None),
                                                    Constant(value='tax_id', kind=None),
                                                    Constant(value='src_tax_id', kind=None),
                                                    Constant(value='tax_repartition_line_id', kind=None),
                                                    Constant(value='base_amount', kind=None),
                                                    Constant(value='tax_amount', kind=None),
                                                    Constant(value='base_amount_currency', kind=None),
                                                    Constant(value='tax_amount_currency', kind=None),
                                                ],
                                                values=[
                                                    Name(id='invoice_line', ctx=Load()),
                                                    Name(id='tax_line', ctx=Load()),
                                                    Name(id='src_line', ctx=Load()),
                                                    Name(id='tax', ctx=Load()),
                                                    IfExp(
                                                        test=Subscript(
                                                            value=Name(id='row', ctx=Load()),
                                                            slice=Constant(value='group_tax_id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        body=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='account.tax', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='browse',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='row', ctx=Load()),
                                                                    slice=Constant(value='group_tax_id', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        orelse=Name(id='tax', ctx=Load()),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='tax_line', ctx=Load()),
                                                        attr='tax_repartition_line_id',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='base_amount', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='tax_amount', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='base_amount_currency', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='tax_amount_currency', kind=None),
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
                            targets=[Name(id='grouping_key_generator', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='grouping_key_generator', ctx=Load()),
                                    Name(id='default_grouping_key_generator', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='move_type',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='out_refund', kind=None),
                                            Constant(value='in_refund', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='tax_rep_lines_field', ctx=Store())],
                                    value=Constant(value='refund_repartition_line_ids', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='tax_rep_lines_field', ctx=Store())],
                                    value=Constant(value='invoice_repartition_line_ids', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='filtered_invoice_lines_tax_values_dict', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='invoice_line', ctx=Store()),
                            iter=Name(id='invoice_lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='tax_values_list', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='invoice_lines_tax_values_dict', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice_line', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='filtered_invoice_lines_tax_values_dict', ctx=Load()),
                                            slice=Name(id='invoice_line', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='taxes_set', ctx=Store())],
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='invoice_line', ctx=Load()),
                                                        attr='tax_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='flatten_taxes_hierarchy',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='tax_values', ctx=Store()),
                                    iter=Name(id='tax_values_list', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='taxes_set', ctx=Load()),
                                                    attr='discard',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='tax_values', ctx=Load()),
                                                        slice=Constant(value='tax_id', kind=None),
                                                        ctx=Load(),
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
                                                        operand=Name(id='filter_to_apply', ctx=Load()),
                                                    ),
                                                    Call(
                                                        func=Name(id='filter_to_apply', ctx=Load()),
                                                        args=[Name(id='tax_values', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='filtered_invoice_lines_tax_values_dict', ctx=Load()),
                                                                slice=Name(id='invoice_line', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='tax_values', ctx=Load())],
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
                                For(
                                    target=Name(id='zero_tax', ctx=Store()),
                                    iter=Name(id='taxes_set', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='affect_base_amount', ctx=Store())],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='affect_base_amount_currency', ctx=Store())],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='tax_values', ctx=Store()),
                                            iter=Name(id='tax_values_list', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='zero_tax', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='tax_values', ctx=Load()),
                                                                    slice=Constant(value='tax_line_id', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='tax_ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='affect_base_amount', ctx=Store()),
                                                            op=Add(),
                                                            value=Subscript(
                                                                value=Name(id='tax_values', ctx=Load()),
                                                                slice=Constant(value='tax_amount', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='affect_base_amount_currency', ctx=Store()),
                                                            op=Add(),
                                                            value=Subscript(
                                                                value=Name(id='tax_values', ctx=Load()),
                                                                slice=Constant(value='tax_amount_currency', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='tax_rep', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='zero_tax', ctx=Load()),
                                                        slice=Name(id='tax_rep_lines_field', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='repartition_type',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='tax', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='tax_values', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='base_line_id', kind=None),
                                                            Constant(value='tax_line_id', kind=None),
                                                            Constant(value='src_line_id', kind=None),
                                                            Constant(value='tax_id', kind=None),
                                                            Constant(value='src_tax_id', kind=None),
                                                            Constant(value='tax_repartition_line_id', kind=None),
                                                            Constant(value='base_amount', kind=None),
                                                            Constant(value='tax_amount', kind=None),
                                                            Constant(value='base_amount_currency', kind=None),
                                                            Constant(value='tax_amount_currency', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='invoice_line', ctx=Load()),
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='account.move.line', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='invoice_line', ctx=Load()),
                                                            Name(id='zero_tax', ctx=Load()),
                                                            Name(id='zero_tax', ctx=Load()),
                                                            Name(id='tax_rep', ctx=Load()),
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='invoice_line', ctx=Load()),
                                                                    attr='balance',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Add(),
                                                                right=Name(id='affect_base_amount', ctx=Load()),
                                                            ),
                                                            Constant(value=0.0, kind=None),
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='invoice_line', ctx=Load()),
                                                                    attr='amount_currency',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Add(),
                                                                right=Name(id='affect_base_amount_currency', ctx=Load()),
                                                            ),
                                                            Constant(value=0.0, kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='filter_to_apply', ctx=Load()),
                                                            ),
                                                            Call(
                                                                func=Name(id='filter_to_apply', ctx=Load()),
                                                                args=[Name(id='tax_values', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='filtered_invoice_lines_tax_values_dict', ctx=Load()),
                                                                        slice=Name(id='invoice_line', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='tax_values', ctx=Load())],
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
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_global_tax_details', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='base_amount', kind=None),
                                    Constant(value='tax_amount', kind=None),
                                    Constant(value='base_amount_currency', kind=None),
                                    Constant(value='tax_amount_currency', kind=None),
                                    Constant(value='tax_details', kind=None),
                                    Constant(value='invoice_line_tax_details', kind=None),
                                ],
                                values=[
                                    Constant(value=0.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Call(
                                        func=Name(id='defaultdict', ctx=Load()),
                                        args=[
                                            Lambda(
                                                args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                                body=Dict(
                                                    keys=[
                                                        Constant(value='base_amount', kind=None),
                                                        Constant(value='tax_amount', kind=None),
                                                        Constant(value='base_amount_currency', kind=None),
                                                        Constant(value='tax_amount_currency', kind=None),
                                                        Constant(value='group_tax_details', kind=None),
                                                    ],
                                                    values=[
                                                        Constant(value=0.0, kind=None),
                                                        Constant(value=0.0, kind=None),
                                                        Constant(value=0.0, kind=None),
                                                        Constant(value=0.0, kind=None),
                                                        List(elts=[], ctx=Load()),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='defaultdict', ctx=Load()),
                                        args=[
                                            Lambda(
                                                args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                                body=Dict(
                                                    keys=[
                                                        Constant(value='base_amount', kind=None),
                                                        Constant(value='tax_amount', kind=None),
                                                        Constant(value='base_amount_currency', kind=None),
                                                        Constant(value='tax_amount_currency', kind=None),
                                                        Constant(value='tax_details', kind=None),
                                                    ],
                                                    values=[
                                                        Constant(value=0.0, kind=None),
                                                        Constant(value=0.0, kind=None),
                                                        Constant(value=0.0, kind=None),
                                                        Constant(value=0.0, kind=None),
                                                        Call(
                                                            func=Name(id='defaultdict', ctx=Load()),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                                                    body=Dict(
                                                                        keys=[
                                                                            Constant(value='base_amount', kind=None),
                                                                            Constant(value='tax_amount', kind=None),
                                                                            Constant(value='base_amount_currency', kind=None),
                                                                            Constant(value='tax_amount_currency', kind=None),
                                                                            Constant(value='group_tax_details', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=0.0, kind=None),
                                                                            Constant(value=0.0, kind=None),
                                                                            Constant(value=0.0, kind=None),
                                                                            Constant(value=0.0, kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='invoice_line', ctx=Store()),
                            iter=Name(id='invoice_lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='tax_values_list', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='filtered_invoice_lines_tax_values_dict', ctx=Load()),
                                        slice=Name(id='invoice_line', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='key_by_tax', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='invoice_global_tax_details', ctx=Load()),
                                        slice=Constant(value='base_amount', kind=None),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Attribute(
                                        value=Name(id='invoice_line', ctx=Load()),
                                        attr='balance',
                                        ctx=Load(),
                                    ),
                                ),
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='invoice_global_tax_details', ctx=Load()),
                                        slice=Constant(value='base_amount_currency', kind=None),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Attribute(
                                        value=Name(id='invoice_line', ctx=Load()),
                                        attr='amount_currency',
                                        ctx=Load(),
                                    ),
                                ),
                                For(
                                    target=Name(id='tax_values', ctx=Store()),
                                    iter=Name(id='tax_values_list', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='grouping_key', ctx=Store())],
                                            value=Call(
                                                func=Name(id='grouping_key_generator', ctx=Load()),
                                                args=[Name(id='tax_values', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='serialized_grouping_key', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_serialize_python_dictionary', ctx=Load()),
                                                args=[Name(id='grouping_key', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='key_by_tax', ctx=Load()),
                                                    slice=Subscript(
                                                        value=Name(id='tax_values', ctx=Load()),
                                                        slice=Constant(value='tax_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='serialized_grouping_key', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='serialized_grouping_key', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='invoice_global_tax_details', ctx=Load()),
                                                            slice=Constant(value='invoice_line_tax_details', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='invoice_line', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='invoice_line_global_tax_details', ctx=Store())],
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='invoice_global_tax_details', ctx=Load()),
                                                            slice=Constant(value='invoice_line_tax_details', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='invoice_line', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='invoice_line_global_tax_details', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='base_amount', kind=None),
                                                                    Constant(value='base_amount_currency', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='invoice_line', ctx=Load()),
                                                                        attr='balance',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='invoice_line', ctx=Load()),
                                                                        attr='amount_currency',
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
                                                    targets=[Name(id='invoice_line_global_tax_details', ctx=Store())],
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='invoice_global_tax_details', ctx=Load()),
                                                            slice=Constant(value='invoice_line_tax_details', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='invoice_line', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_add_edi_tax_values',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='invoice_global_tax_details', ctx=Load()),
                                                    Name(id='grouping_key', ctx=Load()),
                                                    Name(id='serialized_grouping_key', ctx=Load()),
                                                    Name(id='tax_values', ctx=Load()),
                                                    Name(id='key_by_tax', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_add_edi_tax_values',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='invoice_line_global_tax_details', ctx=Load()),
                                                    Name(id='grouping_key', ctx=Load()),
                                                    Name(id='serialized_grouping_key', ctx=Load()),
                                                    Name(id='tax_values', ctx=Load()),
                                                    Name(id='key_by_tax', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='invoice_global_tax_details', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_edi_vals_to_export',
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
                            value=Constant(value=' The purpose of this helper is to prepare values in order to export an invoice through the EDI system.\n        This includes the computation of the tax details for each invoice line that could be very difficult to\n        handle regarding the computation of the base amount.\n\n        :return: A python dict containing default pre-processed values.\n        ', kind=None),
                        ),
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
                            value=Dict(
                                keys=[
                                    Constant(value='record', kind=None),
                                    Constant(value='balance_multiplicator', kind=None),
                                    Constant(value='invoice_line_vals_list', kind=None),
                                ],
                                values=[
                                    Name(id='self', ctx=Load()),
                                    IfExp(
                                        test=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='is_inbound',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        body=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        orelse=Constant(value=1, kind=None),
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='index', ctx=Store()),
                                    Name(id='line', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='invoice_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='line', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='display_type',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='start',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='line_vals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='_prepare_edi_vals_to_export',
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
                                            value=Name(id='line_vals', ctx=Load()),
                                            slice=Constant(value='index', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='index', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='invoice_line_vals_list', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='line_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='total_price_subtotal_before_discount', kind=None),
                                            Constant(value='total_price_discount', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Subscript(
                                                            value=Name(id='x', ctx=Load()),
                                                            slice=Constant(value='price_subtotal_before_discount', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='x', ctx=Store()),
                                                                iter=Subscript(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    slice=Constant(value='invoice_line_vals_list', kind=None),
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
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Subscript(
                                                            value=Name(id='x', ctx=Load()),
                                                            slice=Constant(value='price_discount', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='x', ctx=Store()),
                                                                iter=Subscript(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    slice=Constant(value='invoice_line_vals_list', kind=None),
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
                                ],
                                keywords=[],
                            ),
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
                    name='_update_payments_edi_documents',
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
                            value=Constant(value=' Update the edi documents linked to the current journal entries. These journal entries must be linked to an\n        account.payment of an account.bank.statement.line. This additional method is needed because the payment flow is\n        not the same as the invoice one. Indeed, the edi documents must be updated when the reconciliation with some\n        invoices is changing.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='edi_document_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='payment', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='edi_formats', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='payment', ctx=Load()),
                                                        attr='_get_reconciled_invoices',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='edi_format_ids',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='edi_document_ids',
                                                ctx=Load(),
                                            ),
                                            attr='edi_format_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='edi_formats', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.edi.format', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='edi_formats', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='edi_format', ctx=Store()),
                                    iter=Name(id='edi_formats', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='existing_edi_document', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='payment', ctx=Load()),
                                                        attr='edi_document_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='edi_format_id',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Name(id='edi_format', ctx=Load())],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='edi_format', ctx=Load()),
                                                    attr='_is_required_for_payment',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='payment', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Name(id='existing_edi_document', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='existing_edi_document', ctx=Load()),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='state', kind=None),
                                                                            Constant(value='error', kind=None),
                                                                            Constant(value='blocking_level', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='to_send', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=False, kind=None),
                                                                        ],
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
                                                                    value=Name(id='edi_document_vals_list', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='edi_format_id', kind=None),
                                                                            Constant(value='move_id', kind=None),
                                                                            Constant(value='state', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='edi_format', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='payment', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='to_send', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Name(id='existing_edi_document', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='existing_edi_document', ctx=Load()),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='state', kind=None),
                                                                            Constant(value='error', kind=None),
                                                                            Constant(value='blocking_level', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=False, kind=None),
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
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.edi.document', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='edi_document_vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_process_documents_no_web_services',
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
                    name='_post',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='soft', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='posted', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='soft',
                                        value=Name(id='soft', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='edi_document_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='posted', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='edi_format', ctx=Store()),
                                    iter=Attribute(
                                        value=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Load(),
                                        ),
                                        attr='edi_format_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='is_edi_needed', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='is_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='include_receipts',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='edi_format', ctx=Load()),
                                                            attr='_is_required_for_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='move', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='is_edi_needed', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='errors', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='edi_format', ctx=Load()),
                                                            attr='_check_move_configuration',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='move', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='errors', ctx=Load()),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='UserError', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='Invalid invoice configuration:\n\n%s', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Mod(),
                                                                        right=Call(
                                                                            func=Attribute(
                                                                                value=Constant(value='\n', kind=None),
                                                                                attr='join',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='errors', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='existing_edi_document', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='edi_document_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='x', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='x', ctx=Load()),
                                                                        attr='edi_format_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='edi_format', ctx=Load())],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='existing_edi_document', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='existing_edi_document', ctx=Load()),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='state', kind=None),
                                                                            Constant(value='attachment_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='to_send', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                        ],
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
                                                                    value=Name(id='edi_document_vals_list', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='edi_format_id', kind=None),
                                                                            Constant(value='move_id', kind=None),
                                                                            Constant(value='state', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='edi_format', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='move', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='to_send', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.edi.document', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='edi_document_vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='posted', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_process_documents_no_web_services',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
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
                                        args=[Constant(value='account_edi.ir_cron_edi_network', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_trigger',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='posted', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='button_cancel',
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='button_cancel',
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
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='edi_document_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='doc', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='doc', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value='sent', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='state', kind=None),
                                            Constant(value='error', kind=None),
                                            Constant(value='blocking_level', kind=None),
                                        ],
                                        values=[
                                            Constant(value='cancelled', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='edi_document_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='doc', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='doc', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='sent', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='state', kind=None),
                                            Constant(value='error', kind=None),
                                            Constant(value='blocking_level', kind=None),
                                        ],
                                        values=[
                                            Constant(value='to_cancel', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_process_documents_no_web_services',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
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
                                        args=[Constant(value='account_edi.ir_cron_edi_network', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_trigger',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                    name='button_draft',
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
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='edi_show_cancel_button',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value="You can't edit the following journal entry %s because an electronic document has already been sent. Please use the 'Request EDI Cancellation' button instead.", kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='button_draft',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='error', kind=None),
                                            Constant(value='blocking_level', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                    name='button_cancel_posted_moves',
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
                            value=Constant(value='Mark the edi.document related to this move to be canceled.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='to_cancel_documents', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.edi.document', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='is_move_marked', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='doc', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='doc', ctx=Load()),
                                                                attr='edi_format_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_needs_web_services',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='doc', ctx=Load()),
                                                        attr='attachment_id',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='doc', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='sent', kind=None)],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='is_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='include_receipts',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='doc', ctx=Load()),
                                                                attr='edi_format_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_is_required_for_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='move', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='to_cancel_documents', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Name(id='doc', ctx=Load()),
                                                ),
                                                Assign(
                                                    targets=[Name(id='is_move_marked', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='is_move_marked', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='A cancellation of the EDI has been requested.', kind=None)],
                                                            keywords=[],
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='to_cancel_documents', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='state', kind=None),
                                            Constant(value='error', kind=None),
                                            Constant(value='blocking_level', kind=None),
                                        ],
                                        values=[
                                            Constant(value='to_cancel', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
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
                    name='button_abandon_cancel_posted_posted_moves',
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
                            value=Constant(value='Cancel the request for cancellation of the EDI.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='documents', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.edi.document', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='is_move_marked', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='doc', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='doc', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='to_cancel', kind=None)],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='is_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='include_receipts',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='doc', ctx=Load()),
                                                                attr='edi_format_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_is_required_for_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='move', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='documents', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Name(id='doc', ctx=Load()),
                                                ),
                                                Assign(
                                                    targets=[Name(id='is_move_marked', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='is_move_marked', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='A request for cancellation of the EDI has been called off.', kind=None)],
                                                            keywords=[],
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='documents', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='sent', kind=None)],
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
                    name='_get_edi_document',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='edi_format', annotation=None, type_comment=None),
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='d', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='d', ctx=Load()),
                                                attr='edi_format_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Name(id='edi_format', ctx=Load())],
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
                    name='_get_edi_attachment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='edi_format', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_edi_document',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='edi_format', ctx=Load())],
                                    keywords=[],
                                ),
                                attr='attachment_id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_create_invoice_from_attachment_decoders',
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_create_invoice_from_attachment_decoders',
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
                                    value=Name(id='res', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='account.edi.format', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='search',
                                                        ctx=Load(),
                                                    ),
                                                    args=[List(elts=[], ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='_create_invoice_from_attachment',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
                    name='_get_update_invoice_from_attachment_decoders',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_update_invoice_from_attachment_decoders',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='account.edi.format', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='search',
                                                        ctx=Load(),
                                                    ),
                                                    args=[List(elts=[], ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='_update_invoice_from_attachment',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
                    name='action_process_edi_web_services',
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
                            targets=[Name(id='docs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='d', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='d', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='to_send', kind=None),
                                                                Constant(value='to_cancel', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='d', ctx=Load()),
                                                        attr='blocking_level',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value='error', kind=None)],
                                                ),
                                            ],
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
                                    value=Name(id='docs', ctx=Load()),
                                    attr='_process_documents_web_services',
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
                    name='_retry_edi_documents_error_hook',
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
                            value=Constant(value=" Hook called when edi_documents are retried. For example, when it's needed to clean a field.\n        TO OVERRIDE\n        ", kind=None),
                        ),
                        Return(value=None),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_retry_edi_documents_error',
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
                                    attr='_retry_edi_documents_error_hook',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='error', kind=None),
                                            Constant(value='blocking_level', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='action_process_edi_web_services',
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AccountMoveLine',
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
                    value=Constant(value='account.move.line', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_edi_vals_to_export',
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
                            value=Constant(value=" The purpose of this helper is the same as '_prepare_edi_vals_to_export' but for a single invoice line.\n        This includes the computation of the tax details for each invoice line or the management of the discount.\n        Indeed, in some EDI, we need to provide extra values depending the discount such as:\n        - the discount as an amount instead of a percentage.\n        - the price_unit but after subtraction of the discount.\n\n        :return: A python dict containing default pre-processed values.\n        ", kind=None),
                        ),
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
                            value=Dict(
                                keys=[
                                    Constant(value='line', kind=None),
                                    Constant(value='price_unit_after_discount', kind=None),
                                    Constant(value='price_subtotal_before_discount', kind=None),
                                    Constant(value='price_subtotal_unit', kind=None),
                                    Constant(value='price_total_unit', kind=None),
                                ],
                                values=[
                                    Name(id='self', ctx=Load()),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='price_unit',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=BinOp(
                                            left=Constant(value=1, kind=None),
                                            op=Sub(),
                                            right=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='discount',
                                                    ctx=Load(),
                                                ),
                                                op=Div(),
                                                right=Constant(value=100.0, kind=None),
                                            ),
                                        ),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='round',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='quantity',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    IfExp(
                                        test=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='quantity',
                                            ctx=Load(),
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                attr='round',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                BinOp(
                                                    left=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='price_subtotal',
                                                        ctx=Load(),
                                                    ),
                                                    op=Div(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='quantity',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=0.0, kind=None),
                                    ),
                                    IfExp(
                                        test=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='quantity',
                                            ctx=Load(),
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                attr='round',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                BinOp(
                                                    left=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='price_total',
                                                        ctx=Load(),
                                                    ),
                                                    op=Div(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='quantity',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=0.0, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='price_discount', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='price_subtotal_before_discount', kind=None),
                                    ctx=Load(),
                                ),
                                op=Sub(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='price_subtotal',
                                    ctx=Load(),
                                ),
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
                    name='reconcile',
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
                            targets=[Name(id='all_lines', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='self', ctx=Load()),
                                    op=Add(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='matched_debit_ids',
                                            ctx=Load(),
                                        ),
                                        attr='debit_move_id',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='matched_credit_ids',
                                        ctx=Load(),
                                    ),
                                    attr='credit_move_id',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payments', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='all_lines', ctx=Load()),
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
                                            args=[arg(arg='move', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='payment_id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='statement_line_id',
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
                            targets=[Name(id='invoices_per_payment_before', ctx=Store())],
                            value=DictComp(
                                key=Name(id='pay', ctx=Load()),
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='pay', ctx=Load()),
                                        attr='_get_reconciled_invoices',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='pay', ctx=Store()),
                                        iter=Name(id='payments', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='reconcile',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoices_per_payment_after', ctx=Store())],
                            value=DictComp(
                                key=Name(id='pay', ctx=Load()),
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='pay', ctx=Load()),
                                        attr='_get_reconciled_invoices',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='pay', ctx=Store()),
                                        iter=Name(id='payments', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='changed_payments', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.move', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='payment', ctx=Store()),
                                    Name(id='invoices_after', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='invoices_per_payment_after', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='invoices_before', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='invoices_per_payment_before', ctx=Load()),
                                        slice=Name(id='payment', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='invoices_after', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='invoices_before', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='changed_payments', ctx=Store()),
                                            op=BitOr(),
                                            value=Name(id='payment', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='changed_payments', ctx=Load()),
                                    attr='_update_payments_edi_documents',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                    name='remove_move_reconcile',
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
                            targets=[Name(id='all_lines', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='self', ctx=Load()),
                                    op=Add(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='matched_debit_ids',
                                            ctx=Load(),
                                        ),
                                        attr='debit_move_id',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='matched_credit_ids',
                                        ctx=Load(),
                                    ),
                                    attr='credit_move_id',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payments', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='all_lines', ctx=Load()),
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
                                            args=[arg(arg='move', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='payment_id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='statement_line_id',
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
                            targets=[Name(id='invoices_per_payment_before', ctx=Store())],
                            value=DictComp(
                                key=Name(id='pay', ctx=Load()),
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='pay', ctx=Load()),
                                        attr='_get_reconciled_invoices',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='pay', ctx=Store()),
                                        iter=Name(id='payments', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='remove_move_reconcile',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoices_per_payment_after', ctx=Store())],
                            value=DictComp(
                                key=Name(id='pay', ctx=Load()),
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='pay', ctx=Load()),
                                        attr='_get_reconciled_invoices',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='pay', ctx=Store()),
                                        iter=Name(id='payments', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='changed_payments', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.move', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='payment', ctx=Store()),
                                    Name(id='invoices_after', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='invoices_per_payment_after', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='invoices_before', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='invoices_per_payment_before', ctx=Load()),
                                        slice=Name(id='payment', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='invoices_after', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='invoices_before', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='changed_payments', ctx=Store()),
                                            op=BitOr(),
                                            value=Name(id='payment', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='changed_payments', ctx=Load()),
                                    attr='_update_payments_edi_documents',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
