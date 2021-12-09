Module(
    body=[
        ImportFrom(
            module='odoo.addons.survey.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestSurveyComputePagesQuestions',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TestSurveyCommon',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_compute_pages_questions',
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
                                        args=[Constant(value='survey_manager', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='survey', ctx=Store())],
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
                                                keys=[Constant(value='title', kind=None)],
                                                values=[Constant(value='Test compute survey', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page_0', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='survey.question', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='is_page', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                    Constant(value='title', kind=None),
                                                    Constant(value='survey_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='P1', kind=None),
                                                    Attribute(
                                                        value=Name(id='survey', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page0_q0', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='Q1', kind=None),
                                            Constant(value='text_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page0_q1', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='Q2', kind=None),
                                            Constant(value='text_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page0_q2', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='Q3', kind=None),
                                            Constant(value='text_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page0_q3', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='Q4', kind=None),
                                            Constant(value='text_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page0_q4', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='Q5', kind=None),
                                            Constant(value='text_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page_1', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='survey.question', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='is_page', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                    Constant(value='title', kind=None),
                                                    Constant(value='survey_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Constant(value=7, kind=None),
                                                    Constant(value='P2', kind=None),
                                                    Attribute(
                                                        value=Name(id='survey', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page1_q0', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_1', ctx=Load()),
                                            Constant(value='Q6', kind=None),
                                            Constant(value='text_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page1_q1', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_1', ctx=Load()),
                                            Constant(value='Q7', kind=None),
                                            Constant(value='text_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page1_q2', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_1', ctx=Load()),
                                            Constant(value='Q8', kind=None),
                                            Constant(value='text_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page1_q3', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_1', ctx=Load()),
                                            Constant(value='Q9', kind=None),
                                            Constant(value='text_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='survey', ctx=Load()),
                                                attr='page_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='Survey should have 2 pages', kind=None),
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
                                    Name(id='page_0', ctx=Load()),
                                    Attribute(
                                        value=Name(id='survey', ctx=Load()),
                                        attr='page_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value="Page 1 should be contained in survey's page_ids", kind=None),
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
                                    Name(id='page_1', ctx=Load()),
                                    Attribute(
                                        value=Name(id='survey', ctx=Load()),
                                        attr='page_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value="Page 2 should be contained in survey's page_ids", kind=None),
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
                                                value=Name(id='page_0', ctx=Load()),
                                                attr='question_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=5, kind=None),
                                    Constant(value='Page 1 should have 5 questions', kind=None),
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
                                    Name(id='page0_q0', ctx=Load()),
                                    Attribute(
                                        value=Name(id='page_0', ctx=Load()),
                                        attr='question_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Question 1 should be in page 1', kind=None),
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
                                    Name(id='page0_q1', ctx=Load()),
                                    Attribute(
                                        value=Name(id='page_0', ctx=Load()),
                                        attr='question_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Question 2 should be in page 1', kind=None),
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
                                    Name(id='page0_q2', ctx=Load()),
                                    Attribute(
                                        value=Name(id='page_0', ctx=Load()),
                                        attr='question_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Question 3 should be in page 1', kind=None),
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
                                    Name(id='page0_q3', ctx=Load()),
                                    Attribute(
                                        value=Name(id='page_0', ctx=Load()),
                                        attr='question_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Question 4 should be in page 1', kind=None),
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
                                    Name(id='page0_q4', ctx=Load()),
                                    Attribute(
                                        value=Name(id='page_0', ctx=Load()),
                                        attr='question_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Question 5 should be in page 1', kind=None),
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
                                                value=Name(id='page_1', ctx=Load()),
                                                attr='question_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
                                    Constant(value='Page 2 should have 4 questions', kind=None),
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
                                    Name(id='page1_q0', ctx=Load()),
                                    Attribute(
                                        value=Name(id='page_1', ctx=Load()),
                                        attr='question_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Question 6 should be in page 2', kind=None),
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
                                    Name(id='page1_q1', ctx=Load()),
                                    Attribute(
                                        value=Name(id='page_1', ctx=Load()),
                                        attr='question_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Question 7 should be in page 2', kind=None),
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
                                    Name(id='page1_q2', ctx=Load()),
                                    Attribute(
                                        value=Name(id='page_1', ctx=Load()),
                                        attr='question_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Question 8 should be in page 2', kind=None),
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
                                    Name(id='page1_q3', ctx=Load()),
                                    Attribute(
                                        value=Name(id='page_1', ctx=Load()),
                                        attr='question_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Question 9 should be in page 2', kind=None),
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
                                        value=Name(id='page0_q0', ctx=Load()),
                                        attr='page_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='page_0', ctx=Load()),
                                    Constant(value='Question 1 should belong to page 1', kind=None),
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
                                        value=Name(id='page0_q1', ctx=Load()),
                                        attr='page_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='page_0', ctx=Load()),
                                    Constant(value='Question 2 should belong to page 1', kind=None),
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
                                        value=Name(id='page0_q2', ctx=Load()),
                                        attr='page_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='page_0', ctx=Load()),
                                    Constant(value='Question 3 should belong to page 1', kind=None),
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
                                        value=Name(id='page0_q3', ctx=Load()),
                                        attr='page_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='page_0', ctx=Load()),
                                    Constant(value='Question 4 should belong to page 1', kind=None),
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
                                        value=Name(id='page0_q4', ctx=Load()),
                                        attr='page_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='page_0', ctx=Load()),
                                    Constant(value='Question 5 should belong to page 1', kind=None),
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
                                        value=Name(id='page1_q0', ctx=Load()),
                                        attr='page_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='page_1', ctx=Load()),
                                    Constant(value='Question 6 should belong to page 2', kind=None),
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
                                        value=Name(id='page1_q1', ctx=Load()),
                                        attr='page_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='page_1', ctx=Load()),
                                    Constant(value='Question 7 should belong to page 2', kind=None),
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
                                        value=Name(id='page1_q2', ctx=Load()),
                                        attr='page_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='page_1', ctx=Load()),
                                    Constant(value='Question 8 should belong to page 2', kind=None),
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
                                        value=Name(id='page1_q3', ctx=Load()),
                                        attr='page_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='page_1', ctx=Load()),
                                    Constant(value='Question 9 should belong to page 2', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='page0_q2', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='sequence', kind=None)],
                                        values=[Constant(value=12, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='page0_q2', ctx=Load()),
                                    attr='_compute_page_id',
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
                                        value=Name(id='page0_q2', ctx=Load()),
                                        attr='page_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='page_1', ctx=Load()),
                                    Constant(value='Question 3 should now belong to page 2', kind=None),
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
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
