Module(
    body=[
        ImportFrom(
            module='odoo.addons.website_event_track_live.controllers.track_live',
            names=[alias(name='EventTrackLiveController', asname=None)],
            level=0,
        ),
        ClassDef(
            name='EventTrackLiveQuizController',
            bases=[Name(id='EventTrackLiveController', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_prepare_track_suggestion_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='track', annotation=None, type_comment=None),
                            arg(arg='track_suggestion', annotation=None, type_comment=None),
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
                                        args=[
                                            Name(id='EventTrackLiveQuizController', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_track_suggestion_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='track', ctx=Load()),
                                    Name(id='track_suggestion', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='current_track', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='show_quiz', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='track', ctx=Load()),
                                                attr='quiz_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='track', ctx=Load()),
                                            attr='is_quiz_completed',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
