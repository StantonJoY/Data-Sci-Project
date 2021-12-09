Module(
    body=[
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='tests', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestUi',
            bases=[
                Attribute(
                    value=Name(id='tests', ctx=Load()),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_01_tickets_questions',
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
                            value=Constant(value=' Will execute the tour that fills up two tickets with a few questions answers\n        and then assert that the answers are correctly saved for each attendee. ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='design_fair_event',
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
                                        slice=Constant(value='event.event', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='date_begin', kind=None),
                                            Constant(value='date_end', kind=None),
                                            Constant(value='event_ticket_ids', kind=None),
                                            Constant(value='website_published', kind=None),
                                            Constant(value='question_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Design Fair New York', kind=None),
                                            BinOp(
                                                left=Call(
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
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=15, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            BinOp(
                                                left=Call(
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
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=15, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='start_sale_datetime', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Free', kind=None),
                                                                    BinOp(
                                                                        left=Call(
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
                                                                        op=Sub(),
                                                                        right=Call(
                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='days',
                                                                                    value=Constant(value=15, kind=None),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='start_sale_datetime', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Other', kind=None),
                                                                    BinOp(
                                                                        left=Call(
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
                                                                        op=Sub(),
                                                                        right=Call(
                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='days',
                                                                                    value=Constant(value=15, kind=None),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Meal Type', kind=None),
                                                                    Constant(value='simple_choice', kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[Constant(value='name', kind=None)],
                                                                                        values=[Constant(value='Mixed', kind=None)],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[Constant(value='name', kind=None)],
                                                                                        values=[Constant(value='Vegetarian', kind=None)],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[Constant(value='name', kind=None)],
                                                                                        values=[Constant(value='Pastafarian', kind=None)],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Allergies', kind=None),
                                                                    Constant(value='text_box', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='once_per_order', kind=None),
                                                                    Constant(value='answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='How did you learn about this event?', kind=None),
                                                                    Constant(value='simple_choice', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[Constant(value='name', kind=None)],
                                                                                        values=[Constant(value='Our website', kind=None)],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[Constant(value='name', kind=None)],
                                                                                        values=[Constant(value='Commercials', kind=None)],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[Constant(value='name', kind=None)],
                                                                                        values=[Constant(value='A friend', kind=None)],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/', kind=None),
                                    Constant(value='test_tickets_questions', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='portal', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='registrations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='event.registration', kind=None),
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
                                                    Constant(value='email', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='attendee-a@gmail.com', kind=None),
                                                            Constant(value='attendee-b@gmail.com', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='registrations', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='first_registration', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='registrations', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='reg', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='reg', ctx=Load()),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='attendee-a@gmail.com', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='second_registration', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='registrations', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='reg', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='reg', ctx=Load()),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='attendee-b@gmail.com', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='first_registration', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Attendee A', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='first_registration', ctx=Load()),
                                        attr='phone',
                                        ctx=Load(),
                                    ),
                                    Constant(value='+32499123456', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='second_registration', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Attendee B', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='event_questions', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='registrations', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='event_id.question_ids', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='event_questions', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='first_registration_answers', ctx=Store())],
                            value=Attribute(
                                value=Name(id='first_registration', ctx=Load()),
                                attr='registration_answer_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='first_registration_answers', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='first_registration_answers', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='answer', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='answer', ctx=Load()),
                                                                    attr='question_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='title',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='Meal Type', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='value_answer_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Vegetarian', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='first_registration_answers', ctx=Load()),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='answer', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='answer', ctx=Load()),
                                                                attr='question_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='title',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='Allergies', kind=None)],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='value_text_box',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Fish and Nuts', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='first_registration_answers', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='answer', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='answer', ctx=Load()),
                                                                    attr='question_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='title',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='How did you learn about this event?', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='value_answer_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='A friend', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='second_registration_answers', ctx=Store())],
                            value=Attribute(
                                value=Name(id='second_registration', ctx=Load()),
                                attr='registration_answer_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='second_registration_answers', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='second_registration_answers', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='answer', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='answer', ctx=Load()),
                                                                    attr='question_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='title',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='Meal Type', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='value_answer_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Pastafarian', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='first_registration_answers', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='answer', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='answer', ctx=Load()),
                                                                    attr='question_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='title',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='How did you learn about this event?', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='value_answer_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='A friend', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Name(id='tests', ctx=Load()),
                        attr='tagged',
                        ctx=Load(),
                    ),
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
