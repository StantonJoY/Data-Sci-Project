Module(
    body=[
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_mail_server',
            names=[alias(name='IrMailServer', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.survey.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='HttpCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestCertificationFlow',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TestSurveyCommon',
                    ctx=Load(),
                ),
                Name(id='HttpCase', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_flow_certification',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='survey_user', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='certification', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='survey.survey', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='access_mode', kind=None),
                                                    Constant(value='users_login_required', kind=None),
                                                    Constant(value='questions_layout', kind=None),
                                                    Constant(value='users_can_go_back', kind=None),
                                                    Constant(value='scoring_type', kind=None),
                                                    Constant(value='scoring_success_min', kind=None),
                                                    Constant(value='certification', kind=None),
                                                    Constant(value='certification_mail_template_id', kind=None),
                                                    Constant(value='is_time_limited', kind=None),
                                                    Constant(value='time_limit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='User Certification for SO lines', kind=None),
                                                    Constant(value='public', kind=None),
                                                    Constant(value=True, kind=None),
                                                    Constant(value='page_per_question', kind=None),
                                                    Constant(value=True, kind=None),
                                                    Constant(value='scoring_with_answers', kind=None),
                                                    Constant(value=85.0, kind=None),
                                                    Constant(value=True, kind=None),
                                                    Attribute(
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
                                                            args=[Constant(value='survey.mail_template_certification', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=True, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='q01', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=None, kind=None),
                                            Constant(value="When do you know it's the right time to use the SO line model?", kind=None),
                                            Constant(value='simple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please select an answer', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='certification', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Please stop', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Only on the SO form', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Only on the Survey form', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='Easy, all the time!!!', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=2.0, kind=None),
                                                            ],
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
                                    targets=[Name(id='q02', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=None, kind=None),
                                            Constant(value='On average, how many lines of code do you need when you use SO line widgets?', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please select an answer', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='certification', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='1', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='5', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=2.0, kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='100', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='1000', kind=None)],
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
                                    targets=[Name(id='q03', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=None, kind=None),
                                            Constant(value='What do you think about SO line widgets (not rated)?', kind=None),
                                            Constant(value='text_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=3, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please tell us what you think', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='certification', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='q04', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=None, kind=None),
                                            Constant(value='On a scale of 1 to 10, how much do you like SO line widgets (not rated)?', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=4, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please tell us what you think', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='certification', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='-1', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='0', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='100', kind=None)],
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
                                    targets=[Name(id='q05', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=None, kind=None),
                                            Constant(value='Select all the correct "types" of SO lines', kind=None),
                                            Constant(value='multiple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=5, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='certification', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='sale_order', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='survey_page', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='survey_question', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='a_future_and_yet_unknown_model', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='none', kind=None),
                                                                UnaryOp(
                                                                    op=USub(),
                                                                    operand=Constant(value=1.0, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='user_emp', kind=None),
                                    Constant(value='user_emp', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_start',
                                    ctx=Load(),
                                ),
                                args=[Name(id='certification', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertResponse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value=200, kind=None),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='certification', ctx=Load()),
                                                attr='title',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Time limit for this survey', kind=None),
                                            Constant(value='10 minutes', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user_inputs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.user_input', kind=None),
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
                                                    Constant(value='survey_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='certification', ctx=Load()),
                                                        attr='id',
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
                                        args=[Name(id='user_inputs', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Name(id='user_inputs', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_emp',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='answer_token', ctx=Store())],
                            value=Attribute(
                                value=Name(id='user_inputs', ctx=Load()),
                                attr='access_token',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_page',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='certification', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertResponse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='csrf_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_find_csrf_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_begin',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='certification', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertResponse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='r', ctx=Load()),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='IrMailServer', ctx=Load()),
                                            Constant(value='connect', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_answer_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='q01', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='q01', ctx=Load()),
                                                        attr='suggested_answer_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=3, kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='answer_token', ctx=Load()),
                                            Name(id='csrf_token', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_answer_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='q02', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='q02', ctx=Load()),
                                                        attr='suggested_answer_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='answer_token', ctx=Load()),
                                            Name(id='csrf_token', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_answer_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='q03', ctx=Load()),
                                            Constant(value="I think they're great!", kind=None),
                                            Name(id='answer_token', ctx=Load()),
                                            Name(id='csrf_token', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_answer_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='q04', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='q04', ctx=Load()),
                                                        attr='suggested_answer_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='answer_token', ctx=Load()),
                                            Name(id='csrf_token', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='button_submit',
                                                value=Constant(value='previous', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_answer_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='q03', ctx=Load()),
                                            Constant(value="Just kidding, I don't like it...", kind=None),
                                            Name(id='answer_token', ctx=Load()),
                                            Name(id='csrf_token', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_answer_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='q04', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='q04', ctx=Load()),
                                                        attr='suggested_answer_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='answer_token', ctx=Load()),
                                            Name(id='csrf_token', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_answer_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='q05', ctx=Load()),
                                            List(
                                                elts=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='q05', ctx=Load()),
                                                                attr='suggested_answer_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='q05', ctx=Load()),
                                                                attr='suggested_answer_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='q05', ctx=Load()),
                                                                attr='suggested_answer_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=3, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Name(id='answer_token', ctx=Load()),
                                            Name(id='csrf_token', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_inputs', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        value=Name(id='user_inputs', ctx=Load()),
                                        attr='scoring_percentage',
                                        ctx=Load(),
                                    ),
                                    Constant(value=87.5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='user_inputs', ctx=Load()),
                                        attr='scoring_success',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='certification', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='scoring_success_min', kind=None)],
                                        values=[Constant(value=90, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='user_inputs', ctx=Load()),
                                        attr='scoring_success',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="I think they're great!", kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='user_inputs', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_input_line_ids.value_text_box', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="Just kidding, I don't like it...", kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='user_inputs', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_input_line_ids.value_text_box', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='certification_email', ctx=Store())],
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
                                                slice=Constant(value='mail.mail', kind=None),
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
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Constant(value='create_date desc', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='User Certification for SO lines', kind=None),
                                    Attribute(
                                        value=Name(id='certification_email', ctx=Load()),
                                        attr='subject',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='employee@example.com', kind=None),
                                    Attribute(
                                        value=Name(id='certification_email', ctx=Load()),
                                        attr='email_to',
                                        ctx=Load(),
                                    ),
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='certification_email', ctx=Load()),
                                                attr='attachment_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='certification_email', ctx=Load()),
                                                attr='attachment_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Certification Document.html', kind=None),
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
                    name='test_randomized_certification',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='survey_user', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='certification', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='survey.survey', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='questions_layout', kind=None),
                                                    Constant(value='questions_selection', kind=None),
                                                    Constant(value='scoring_type', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='User randomized Certification', kind=None),
                                                    Constant(value='page_per_section', kind=None),
                                                    Constant(value='random', kind=None),
                                                    Constant(value='scoring_without_answers', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page1', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=None, kind=None),
                                            Constant(value='Page 1', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='certification', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='is_page',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='random_questions_count',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='q101', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=None, kind=None),
                                            Constant(value='What is the answer to the first question?', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please select an answer', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='certification', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='The correct answer', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='The wrong answer', kind=None)],
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
                                    targets=[Name(id='q102', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=None, kind=None),
                                            Constant(value='What is the answer to the second question?', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=3, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please select an answer', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='certification', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='The correct answer', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='The wrong answer', kind=None)],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='user_emp', kind=None),
                                    Constant(value='user_emp', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_start',
                                    ctx=Load(),
                                ),
                                args=[Name(id='certification', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_inputs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.user_input', kind=None),
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
                                                    Constant(value='survey_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='certification', ctx=Load()),
                                                        attr='id',
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
                                        args=[Name(id='user_inputs', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Name(id='user_inputs', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_emp',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='answer_token', ctx=Store())],
                            value=Attribute(
                                value=Name(id='user_inputs', ctx=Load()),
                                attr='access_token',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_page',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='certification', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertResponse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='csrf_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_find_csrf_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_begin',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='certification', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertResponse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='r', ctx=Load()),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='IrMailServer', ctx=Load()),
                                            Constant(value='connect', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='question_ids', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='user_inputs', ctx=Load()),
                                        attr='predefined_question_ids',
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
                                                args=[Name(id='question_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value=1, kind=None),
                                            Constant(value='Only one question should have been selected by the randomization', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_answer_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='question_ids', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='question_ids', ctx=Load()),
                                                        attr='suggested_answer_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='answer_token', ctx=Load()),
                                            Name(id='csrf_token', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='statistics', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='user_inputs', ctx=Load()),
                                        attr='_prepare_statistics',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Name(id='user_inputs', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='total_statistics', ctx=Store())],
                            value=Subscript(
                                value=Name(id='statistics', ctx=Load()),
                                slice=Constant(value='totals', kind=None),
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
                                    Name(id='total_statistics', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='text', kind=None),
                                                    Constant(value='count', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Correct', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='text', kind=None),
                                                    Constant(value='count', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Partially', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='text', kind=None),
                                                    Constant(value='count', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Incorrect', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='text', kind=None),
                                                    Constant(value='count', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Unanswered', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='With the configured randomization, there should be exactly 1 correctly answered question and none skipped.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='section_statistics', ctx=Store())],
                            value=Subscript(
                                value=Name(id='statistics', ctx=Load()),
                                slice=Constant(value='by_section', kind=None),
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
                                    Name(id='section_statistics', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='Page 1', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='question_count', kind=None),
                                                    Constant(value='correct', kind=None),
                                                    Constant(value='partial', kind=None),
                                                    Constant(value='incorrect', kind=None),
                                                    Constant(value='skipped', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Constant(value="With the configured randomization, there should be exactly 1 correctly answered question in the 'Page 1' section.", kind=None),
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
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                        Constant(value='functional', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
