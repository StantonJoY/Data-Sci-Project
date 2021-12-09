Module(
    body=[
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website_event.controllers.main',
            names=[alias(name='WebsiteEventController', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteEvent',
            bases=[Name(id='WebsiteEventController', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_process_attendees_form',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='form_details', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Process data posted from the attendee details form.\n        Extracts question answers:\n        - For both questions asked 'once_per_order' and questions asked to every attendee\n        - For questions of type 'simple_choice', extracting the suggested answer id\n        - For questions of type 'text_box', extracting the text answer of the attendee. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='registrations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='WebsiteEvent', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_process_attendees_form',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='event', ctx=Load()),
                                    Name(id='form_details', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='registration', ctx=Store()),
                            iter=Name(id='registrations', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='registration', ctx=Load()),
                                            slice=Constant(value='registration_answer_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='general_answer_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='form_details', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='question_answer', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='key', ctx=Load())],
                                            ),
                                            Name(id='value', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='dummy', ctx=Store()),
                                                        Name(id='registration_index', ctx=Store()),
                                                        Name(id='question_id', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='key', ctx=Load()),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='-', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='question_sudo', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='event.question', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[Name(id='question_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='answer_values', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='question_sudo', ctx=Load()),
                                                    attr='question_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='simple_choice', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='answer_values', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='question_id', kind=None),
                                                            Constant(value='value_answer_id', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[Name(id='question_id', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[Name(id='value', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='question_sudo', ctx=Load()),
                                                            attr='question_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='text_box', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='answer_values', ctx=Store())],
                                                            value=Dict(
                                                                keys=[
                                                                    Constant(value='question_id', kind=None),
                                                                    Constant(value='value_text_box', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='int', ctx=Load()),
                                                                        args=[Name(id='question_id', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    Name(id='value', ctx=Load()),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='answer_values', ctx=Load()),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(id='int', ctx=Load()),
                                                            args=[Name(id='registration_index', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='general_answer_ids', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Name(id='answer_values', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Name(id='answer_values', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Subscript(
                                                                            value=Name(id='registrations', ctx=Load()),
                                                                            slice=BinOp(
                                                                                left=Call(
                                                                                    func=Name(id='int', ctx=Load()),
                                                                                    args=[Name(id='registration_index', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Sub(),
                                                                                right=Constant(value=1, kind=None),
                                                                            ),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='registration_answer_ids', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Name(id='answer_values', ctx=Load()),
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
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='registration', ctx=Store()),
                            iter=Name(id='registrations', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='registration', ctx=Load()),
                                                slice=Constant(value='registration_answer_ids', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='general_answer_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='registrations', ctx=Load()),
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
