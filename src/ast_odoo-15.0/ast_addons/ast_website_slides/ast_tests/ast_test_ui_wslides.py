Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tests', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.fields',
            names=[alias(name='Datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_module_resource', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.tests.common',
            names=[
                alias(name='HttpCaseWithUserDemo', asname=None),
                alias(name='HttpCaseWithUserPortal', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestUICommon',
            bases=[
                Name(id='HttpCaseWithUserDemo', ctx=Load()),
                Name(id='HttpCaseWithUserPortal', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                        args=[
                                            Name(id='TestUICommon', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='pdf_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_module_resource', ctx=Load()),
                                args=[
                                    Constant(value='website_slides', kind=None),
                                    Constant(value='static', kind=None),
                                    Constant(value='src', kind=None),
                                    Constant(value='img', kind=None),
                                    Constant(value='presentation.pdf', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pdf_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64encode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='open', ctx=Load()),
                                                args=[
                                                    Name(id='pdf_path', ctx=Load()),
                                                    Constant(value='rb', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='read',
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
                        Assign(
                            targets=[Name(id='img_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_module_resource', ctx=Load()),
                                args=[
                                    Constant(value='website_slides', kind=None),
                                    Constant(value='static', kind=None),
                                    Constant(value='src', kind=None),
                                    Constant(value='img', kind=None),
                                    Constant(value='slide_demo_gardening_1.jpg', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='img_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64encode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='open', ctx=Load()),
                                                args=[
                                                    Name(id='img_path', ctx=Load()),
                                                    Constant(value='rb', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='read',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='slide.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='enroll', kind=None),
                                            Constant(value='channel_type', kind=None),
                                            Constant(value='allow_comment', kind=None),
                                            Constant(value='promote_strategy', kind=None),
                                            Constant(value='is_published', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='create_date', kind=None),
                                            Constant(value='slide_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Basics of Gardening - Test', kind=None),
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
                                                    args=[Constant(value='base.user_admin', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='public', kind=None),
                                            Constant(value='training', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='most_voted', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='Learn the basics of gardening !', kind=None),
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='Datetime', ctx=Load()),
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
                                                            value=Constant(value=8, kind=None),
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
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='datas', kind=None),
                                                                    Constant(value='slide_type', kind=None),
                                                                    Constant(value='is_published', kind=None),
                                                                    Constant(value='is_preview', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Gardening: The Know-How', kind=None),
                                                                    Constant(value=1, kind=None),
                                                                    Name(id='pdf_content', ctx=Load()),
                                                                    Constant(value='presentation', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=True, kind=None),
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
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='image_1920', kind=None),
                                                                    Constant(value='slide_type', kind=None),
                                                                    Constant(value='is_published', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Home Gardening', kind=None),
                                                                    Constant(value=2, kind=None),
                                                                    Name(id='img_content', ctx=Load()),
                                                                    Constant(value='infographic', kind=None),
                                                                    Constant(value=True, kind=None),
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
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='image_1920', kind=None),
                                                                    Constant(value='slide_type', kind=None),
                                                                    Constant(value='is_published', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Mighty Carrots', kind=None),
                                                                    Constant(value=3, kind=None),
                                                                    Name(id='img_content', ctx=Load()),
                                                                    Constant(value='infographic', kind=None),
                                                                    Constant(value=True, kind=None),
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
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='datas', kind=None),
                                                                    Constant(value='slide_type', kind=None),
                                                                    Constant(value='is_published', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='How to Grow and Harvest The Best Strawberries | Basics', kind=None),
                                                                    Constant(value=4, kind=None),
                                                                    Name(id='pdf_content', ctx=Load()),
                                                                    Constant(value='document', kind=None),
                                                                    Constant(value=True, kind=None),
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
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='slide_type', kind=None),
                                                                    Constant(value='is_published', kind=None),
                                                                    Constant(value='question_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Test your knowledge', kind=None),
                                                                    Constant(value=5, kind=None),
                                                                    Constant(value='quiz', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='question', kind=None),
                                                                                            Constant(value='answer_ids', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='What is a strawberry ?', kind=None),
                                                                                            List(
                                                                                                elts=[
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value=0, kind=None),
                                                                                                            Constant(value=0, kind=None),
                                                                                                            Dict(
                                                                                                                keys=[
                                                                                                                    Constant(value='text_value', kind=None),
                                                                                                                    Constant(value='is_correct', kind=None),
                                                                                                                    Constant(value='sequence', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    Constant(value='A fruit', kind=None),
                                                                                                                    Constant(value=True, kind=None),
                                                                                                                    Constant(value=1, kind=None),
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
                                                                                                                    Constant(value='text_value', kind=None),
                                                                                                                    Constant(value='sequence', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    Constant(value='A vegetable', kind=None),
                                                                                                                    Constant(value=2, kind=None),
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
                                                                                                                    Constant(value='text_value', kind=None),
                                                                                                                    Constant(value='sequence', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    Constant(value='A table', kind=None),
                                                                                                                    Constant(value=3, kind=None),
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
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='question', kind=None),
                                                                                            Constant(value='answer_ids', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='What is the best tool to dig a hole for your plants ?', kind=None),
                                                                                            List(
                                                                                                elts=[
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value=0, kind=None),
                                                                                                            Constant(value=0, kind=None),
                                                                                                            Dict(
                                                                                                                keys=[
                                                                                                                    Constant(value='text_value', kind=None),
                                                                                                                    Constant(value='is_correct', kind=None),
                                                                                                                    Constant(value='sequence', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    Constant(value='A shovel', kind=None),
                                                                                                                    Constant(value=True, kind=None),
                                                                                                                    Constant(value=1, kind=None),
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
                                                                                                                    Constant(value='text_value', kind=None),
                                                                                                                    Constant(value='sequence', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    Constant(value='A spoon', kind=None),
                                                                                                                    Constant(value=2, kind=None),
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
            name='TestUi',
            bases=[Name(id='TestUICommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_course_member_employee',
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
                            targets=[Name(id='user_demo', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='user_demo',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='karma', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
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
                                                                    args=[Constant(value='base.group_user', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='ids',
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browser_js',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/slides', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].run("course_member")', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].tours.course_member.ready', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Attribute(
                                            value=Name(id='user_demo', ctx=Load()),
                                            attr='login',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_course_member_elearning_officer',
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
                            targets=[Name(id='user_demo', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='user_demo',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='karma', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=BinOp(
                                                                    left=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='ref',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='base.group_user', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    op=BitOr(),
                                                                    right=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='ref',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='website_slides.group_website_slides_officer', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                attr='ids',
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browser_js',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/slides', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].run("course_member")', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].tours.course_member.ready', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Attribute(
                                            value=Name(id='user_demo', ctx=Load()),
                                            attr='login',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_course_member_portal',
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
                            targets=[Name(id='user_portal', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='user_portal',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_portal', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='user_portal', ctx=Load()),
                                    attr='karma',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=1, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browser_js',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/slides', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].run("course_member")', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].tours.course_member.ready', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Attribute(
                                            value=Name(id='user_portal', ctx=Load()),
                                            attr='login',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_full_screen_edition_website_publisher',
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
                            targets=[Name(id='user_demo', ctx=Store())],
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
                                args=[Constant(value='base.user_demo', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='groups_id', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
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
                                                                    args=[Constant(value='base.group_user', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
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
                                                                    args=[Constant(value='website.group_website_publisher', kind=None)],
                                                                    keywords=[],
                                                                ),
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browser_js',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/slides', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].run("full_screen_web_editor")', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].tours.full_screen_web_editor.ready', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Attribute(
                                            value=Name(id='user_demo', ctx=Load()),
                                            attr='login',
                                            ctx=Load(),
                                        ),
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
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='tests', ctx=Load()),
                            attr='common',
                            ctx=Load(),
                        ),
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
        ClassDef(
            name='TestUiYoutube',
            bases=[Name(id='HttpCaseWithUserDemo', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_course_member_yt_employee',
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
                            targets=[Name(id='user_demo', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='user_demo',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='groups_id', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
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
                                                                    args=[Constant(value='base.group_user', kind=None)],
                                                                    keywords=[],
                                                                ),
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
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website_slides.slide_channel_demo_3_furn0', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_remove_membership',
                                    ctx=Load(),
                                ),
                                args=[
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
                                            args=[Constant(value='base.partner_demo', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='ids',
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
                                    attr='browser_js',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/slides', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].run("course_member_youtube")', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].tours.course_member_youtube.ready', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Attribute(
                                            value=Name(id='user_demo', ctx=Load()),
                                            attr='login',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_course_publisher_elearning_manager',
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
                            targets=[Name(id='user_demo', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='user_demo',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='groups_id', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
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
                                                                    args=[Constant(value='base.group_user', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
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
                                                                    args=[Constant(value='website_slides.group_website_slides_manager', kind=None)],
                                                                    keywords=[],
                                                                ),
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browser_js',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/slides', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].run("course_publisher")', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].tours.course_publisher.ready', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Attribute(
                                            value=Name(id='user_demo', ctx=Load()),
                                            attr='login',
                                            ctx=Load(),
                                        ),
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
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='tests', ctx=Load()),
                            attr='common',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(value='external', kind=None),
                        Constant(value='post_install', kind=None),
                        Constant(value='-standard', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
