Module(
    body=[
        ImportFrom(
            module='werkzeug.exceptions',
            names=[alias(name='Forbidden', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website_event_track.controllers.event_track',
            names=[alias(name='EventTrackController', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteEventTrackQuiz',
            bases=[Name(id='EventTrackController', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='event_track_quiz_submit',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event_id', annotation=None, type_comment=None),
                            arg(arg='track_id', annotation=None, type_comment=None),
                            arg(arg='answer_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
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
                                args=[Name(id='track_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='track_sudo', ctx=Store())],
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
                            targets=[Name(id='event_track_visitor', ctx=Store())],
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
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='visitor_sudo', ctx=Store())],
                            value=Attribute(
                                value=Name(id='event_track_visitor', ctx=Load()),
                                attr='visitor_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='event_track_visitor', ctx=Load()),
                                attr='quiz_completed',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='track_quiz_done', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='answers_details', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_quiz_answers_details',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='track_sudo', ctx=Load()),
                                    Name(id='answer_ids', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='answers_details', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='error', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Name(id='answers_details', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event_track_visitor', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quiz_completed', kind=None),
                                            Constant(value='quiz_points', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Subscript(
                                                value=Name(id='answers_details', ctx=Load()),
                                                slice=Constant(value='points', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='answers', kind=None),
                                    Constant(value='quiz_completed', kind=None),
                                    Constant(value='quiz_points', kind=None),
                                ],
                                values=[
                                    DictComp(
                                        key=Attribute(
                                            value=Attribute(
                                                value=Name(id='answer', ctx=Load()),
                                                attr='question_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        value=Dict(
                                            keys=[
                                                Constant(value='awarded_points', kind=None),
                                                Constant(value='correct_answer', kind=None),
                                                Constant(value='is_correct', kind=None),
                                                Constant(value='comment', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='answer', ctx=Load()),
                                                    attr='awarded_points',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='answer', ctx=Load()),
                                                            attr='question_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='correct_answer_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='text_value',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='answer', ctx=Load()),
                                                    attr='is_correct',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='answer', ctx=Load()),
                                                    attr='comment',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='answer', ctx=Store()),
                                                iter=Subscript(
                                                    value=Name(id='answers_details', ctx=Load()),
                                                    slice=Constant(value='user_answers', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='event_track_visitor', ctx=Load()),
                                        attr='quiz_completed',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='answers_details', ctx=Load()),
                                        slice=Constant(value='points', kind=None),
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
                                    Name(id='visitor_sudo', ctx=Load()),
                                    Compare(
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
                            args=[Constant(value='/event_track/quiz/submit', kind=None)],
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
                    name='quiz_reset',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event_id', annotation=None, type_comment=None),
                            arg(arg='track_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
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
                                args=[Name(id='track_id', ctx=Load())],
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
                                            args=[Constant(value='event.group_event_manager', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='track', ctx=Load()),
                                                        attr='sudo',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='quiz_id',
                                                ctx=Load(),
                                            ),
                                            attr='repeatable',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
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
                            targets=[Name(id='event_track_visitor', ctx=Store())],
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
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event_track_visitor', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quiz_completed', kind=None),
                                            Constant(value='quiz_points', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=0, kind=None),
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
                            args=[Constant(value='/event_track/quiz/reset', kind=None)],
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
                    name='_get_quiz_answers_details',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='track', annotation=None, type_comment=None),
                            arg(arg='answer_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='questions_count', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='track', ctx=Load()),
                                        attr='quiz_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_answers', ctx=Store())],
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
                                                slice=Constant(value='event.quiz.answer', kind=None),
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
                                                    Name(id='answer_ids', ctx=Load()),
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
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='user_answers', ctx=Load()),
                                                attr='mapped',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='question_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Name(id='questions_count', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='quiz_incomplete', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='user_answers', kind=None),
                                    Constant(value='points', kind=None),
                                ],
                                values=[
                                    Name(id='user_answers', ctx=Load()),
                                    Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Name(id='answer', ctx=Load()),
                                                    attr='awarded_points',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='answer', ctx=Store()),
                                                        iter=Name(id='user_answers', ctx=Load()),
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
