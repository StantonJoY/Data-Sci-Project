Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            name='MailThread',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='mail.thread', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_message_post_process_attachments',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attachments', annotation=None, type_comment=None),
                            arg(arg='attachment_ids', annotation=None, type_comment=None),
                            arg(arg='message_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' This method extension ensures that, when using the "Send & Print" feature, if the user\n        adds an attachment, the latter will be linked to the record. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='attached_to', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='record', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='account.move', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='message_values', ctx=Load()),
                                            slice=Constant(value='model', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='message_values', ctx=Load()),
                                            slice=Constant(value='res_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                                    attr='_message_post_process_attachments',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='attachments', ctx=Load()),
                                    Name(id='attachment_ids', ctx=Load()),
                                    Name(id='message_values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Name(id='message_values', ctx=Load()),
                                slice=Constant(value='model', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_id', ctx=Store())],
                            value=Subscript(
                                value=Name(id='message_values', ctx=Load()),
                                slice=Constant(value='res_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='att_ids', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='att', ctx=Load()),
                                    slice=Constant(value=1, kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='att', ctx=Store()),
                                        iter=BoolOp(
                                            op=Or(),
                                            values=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='res', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='attachment_ids', kind=None)],
                                                    keywords=[],
                                                ),
                                                List(elts=[], ctx=Load()),
                                            ],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='att_ids', ctx=Load()),
                                    Compare(
                                        left=Name(id='model', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='account.move', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='filtered_attachment_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
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
                                                                slice=Constant(value='ir.attachment', kind=None),
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
                                                args=[Name(id='att_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='a', annotation=None, type_comment=None)],
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
                                                                value=Name(id='a', ctx=Load()),
                                                                attr='res_model',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[In()],
                                                            comparators=[
                                                                Tuple(
                                                                    elts=[Constant(value='account.invoice.send', kind=None)],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='a', ctx=Load()),
                                                                    attr='create_uid',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_uid',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='filtered_attachment_ids', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='filtered_attachment_ids', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='res_model', kind=None),
                                                            Constant(value='res_id', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='model', ctx=Load()),
                                                            Name(id='res_id', ctx=Load()),
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
