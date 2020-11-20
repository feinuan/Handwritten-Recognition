def get_trainer(self):

    # 获取分类器
    out = convolutional_neural_network()

    # 定义标签
    label = paddle.layer.data(name="label",
                              type=paddle.data_type.integer_value(10))

    # 获取损失函数
    cost = paddle.layer.classification_cost(input=out, label=label)

    # 获取参数
    parameters = paddle.parameters.create(layers=cost)

    """
    定义优化方法
    learning_rate 迭代的速度
    momentum 跟前面动量优化的比例
    regularzation 正则化,防止过拟合
    :leng re
    """
    optimizer = paddle.optimizer.Momentum(learning_rate=0.1 / 128.0,
                                          momentum=0.9,
                                          regularization=paddle.optimizer.L2Regularization(rate=0.0005 * 128))
    '''
    创建训练器
    cost 损失函数
    parameters 训练参数,可以通过创建,也可以使用之前训练好的参数
    update_equation 优化方法
    '''
    trainer = paddle.trainer.SGD(cost=cost,
                                 parameters=parameters,
                                 update_equation=optimizer)
    return trainer