Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='KARMA', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='ask', kind=None),
                    Constant(value='ans', kind=None),
                    Constant(value='com_own', kind=None),
                    Constant(value='com_all', kind=None),
                    Constant(value='com_conv_all', kind=None),
                    Constant(value='upv', kind=None),
                    Constant(value='dwv', kind=None),
                    Constant(value='edit_own', kind=None),
                    Constant(value='edit_all', kind=None),
                    Constant(value='close_own', kind=None),
                    Constant(value='close_all', kind=None),
                    Constant(value='unlink_own', kind=None),
                    Constant(value='unlink_all', kind=None),
                    Constant(value='post', kind=None),
                    Constant(value='flag', kind=None),
                    Constant(value='moderate', kind=None),
                    Constant(value='gen_que_new', kind=None),
                    Constant(value='gen_que_upv', kind=None),
                    Constant(value='gen_que_dwv', kind=None),
                    Constant(value='gen_ans_upv', kind=None),
                    Constant(value='gen_ans_dwv', kind=None),
                    Constant(value='gen_ans_flag', kind=None),
                    Constant(value='tag_create', kind=None),
                ],
                values=[
                    Constant(value=5, kind=None),
                    Constant(value=10, kind=None),
                    Constant(value=5, kind=None),
                    Constant(value=10, kind=None),
                    Constant(value=50, kind=None),
                    Constant(value=5, kind=None),
                    Constant(value=10, kind=None),
                    Constant(value=10, kind=None),
                    Constant(value=20, kind=None),
                    Constant(value=10, kind=None),
                    Constant(value=20, kind=None),
                    Constant(value=10, kind=None),
                    Constant(value=20, kind=None),
                    Constant(value=100, kind=None),
                    Constant(value=500, kind=None),
                    Constant(value=1000, kind=None),
                    Constant(value=1, kind=None),
                    Constant(value=5, kind=None),
                    UnaryOp(
                        op=USub(),
                        operand=Constant(value=10, kind=None),
                    ),
                    Constant(value=10, kind=None),
                    UnaryOp(
                        op=USub(),
                        operand=Constant(value=20, kind=None),
                    ),
                    UnaryOp(
                        op=USub(),
                        operand=Constant(value=45, kind=None),
                    ),
                    Constant(value=30, kind=None),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='TestForumCommon',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
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
                                        args=[
                                            Name(id='TestForumCommon', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
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
                            targets=[Name(id='Forum', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='forum.forum', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Post', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='forum.post', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='TestUsersEnv', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='no_reset_password', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_employee_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.group_user', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_portal_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.group_portal', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_public_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.group_public', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_employee',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='TestUsersEnv', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='karma', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Armande Employee', kind=None),
                                            Constant(value='Armande', kind=None),
                                            Constant(value='armande.employee@example.com', kind=None),
                                            Constant(value=0, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[Name(id='group_employee_id', ctx=Load())],
                                                                ctx=Load(),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_portal',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='TestUsersEnv', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='karma', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Beatrice Portal', kind=None),
                                            Constant(value='Beatrice', kind=None),
                                            Constant(value='beatrice.employee@example.com', kind=None),
                                            Constant(value=0, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[Name(id='group_portal_id', ctx=Load())],
                                                                ctx=Load(),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_public',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='TestUsersEnv', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='karma', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Cedric Public', kind=None),
                                            Constant(value='Cedric', kind=None),
                                            Constant(value='cedric.employee@example.com', kind=None),
                                            Constant(value=0, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[Name(id='group_public_id', ctx=Load())],
                                                                ctx=Load(),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='forum',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Forum', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='karma_ask', kind=None),
                                            Constant(value='karma_answer', kind=None),
                                            Constant(value='karma_comment_own', kind=None),
                                            Constant(value='karma_comment_all', kind=None),
                                            Constant(value='karma_answer_accept_own', kind=None),
                                            Constant(value='karma_answer_accept_all', kind=None),
                                            Constant(value='karma_upvote', kind=None),
                                            Constant(value='karma_downvote', kind=None),
                                            Constant(value='karma_edit_own', kind=None),
                                            Constant(value='karma_edit_all', kind=None),
                                            Constant(value='karma_close_own', kind=None),
                                            Constant(value='karma_close_all', kind=None),
                                            Constant(value='karma_unlink_own', kind=None),
                                            Constant(value='karma_unlink_all', kind=None),
                                            Constant(value='karma_post', kind=None),
                                            Constant(value='karma_comment_convert_all', kind=None),
                                            Constant(value='karma_gen_question_new', kind=None),
                                            Constant(value='karma_gen_question_upvote', kind=None),
                                            Constant(value='karma_gen_question_downvote', kind=None),
                                            Constant(value='karma_gen_answer_upvote', kind=None),
                                            Constant(value='karma_gen_answer_downvote', kind=None),
                                            Constant(value='karma_gen_answer_accept', kind=None),
                                            Constant(value='karma_gen_answer_accepted', kind=None),
                                            Constant(value='karma_gen_answer_flagged', kind=None),
                                        ],
                                        values=[
                                            Constant(value='TestForum', kind=None),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='ask', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='ans', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='com_own', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='com_all', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=9999, kind=None),
                                            Constant(value=9999, kind=None),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='upv', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='dwv', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='edit_own', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='edit_all', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='close_own', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='close_all', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='unlink_own', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='unlink_all', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='post', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='com_conv_all', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='gen_que_new', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='gen_que_upv', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='gen_que_dwv', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='gen_ans_upv', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='gen_ans_dwv', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=9999, kind=None),
                                            Constant(value=9999, kind=None),
                                            Subscript(
                                                value=Name(id='KARMA', ctx=Load()),
                                                slice=Constant(value='gen_ans_flag', kind=None),
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='post',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Post', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='content', kind=None),
                                            Constant(value='forum_id', kind=None),
                                            Constant(value='tag_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='TestQuestion', kind=None),
                                            Constant(value='I am not a bird.', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='forum',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
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
                                                                    Constant(value='forum_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Tag2', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='forum',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='answer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Post', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='content', kind=None),
                                            Constant(value='forum_id', kind=None),
                                            Constant(value='parent_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='TestAnswer', kind=None),
                                            Constant(value='I am an anteater.', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='forum',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='post',
                                                    ctx=Load(),
                                                ),
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
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
